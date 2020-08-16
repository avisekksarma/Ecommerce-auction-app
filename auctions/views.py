from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages

from .models import *
from .forms import *


def index(request):
    active_listings = Listings.objects.filter(status='active')
    active_listings = active_listings.order_by('-id')
    context = {
        'listings': active_listings,
        'is_category': False
    }
    return render(request, "auctions/index.html", context)


def closed_listings_view(request):
    if request.method == "POST":
        if request.POST.get('close', None) == 'close':
            listing = Listings.objects.get(pk=int(request.POST['listing_id']))
            try:
                is_atleast_a_bid_made = (listing.bid is not None)
            except AttributeError:
                is_atleast_a_bid_made = False
            if is_atleast_a_bid_made:
                listing.status = "closed"
                listing.save()
                return HttpResponseRedirect(reverse("closedlistings"))
            else:
                messages.error(request, 'You cannot close the listing until at least a bid is made.')
                return HttpResponseRedirect(reverse("listingdetail", args=(listing.id,)))
    closed_listings = Listings.objects.filter(status='closed')
    closed_listings = closed_listings.order_by('-id')
    context = {
        'listings': closed_listings,
    }
    return render(request, "auctions/closed_listings.html", context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def createlistings(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = User.objects.get(username=request.user)
            listing.save()
            messages.success(request, 'New Listing is created successfully!!')
            return HttpResponseRedirect(reverse('index'))
    context = {"form": form}
    return render(request, 'auctions/createlistings.html', context)


def listing_detail(request, listing_id):
    # request.user.username = '' if user is anonymous user

    if request.method == "POST" and request.POST.get('bid', None) and request.user.is_authenticated:
        bid_handler(listing_id, request)
    if request.method == "POST" and request.POST.get('comment', None) and request.user.is_authenticated:
        comment_handler(listing_id, request)
    if request.method == "POST" and (not request.user.is_authenticated):
        messages.error(request, 'Please login before bidding or commenting.')
    # GET request region
    try:
        listing = Listings.objects.get(pk=listing_id)
        is_my_listing = listing.user.username == request.user.username
    except ObjectDoesNotExist:
        listing = None
        is_my_listing = False

    try:
        comments = listing.comment.all()
    except AttributeError:  # None type has no attribute error if listing is None
        comments = None

    try:
        is_in_watchlist = listing.watchlists.filter(user=User.objects.get(username=request.user)).first() is not None
    except (AttributeError, User.DoesNotExist):
        is_in_watchlist = False

    try:
        bid = listing.bid
    except AttributeError:
        bid = None

    context = {"listing": listing,
               "comments": comments,
               "bid": bid,
               "is_in_watchlist": is_in_watchlist,
               "is_my_listing": is_my_listing
               }
    return render(request, 'auctions/listingdetail.html', context)


# this does not take requests directly from the user but does logic on storing bid made by user.
def bid_handler(listing_id, request):
    print("user=>", request.user.username)
    print("user=>", type(request.user.username))
    listing = Listings.objects.get(pk=listing_id)
    try:
        bid_now = listing.bid.current_bid
        x = "update_bid"
    except ObjectDoesNotExist:
        bid_now = listing.initial_bid
        x = "new_bid"
    if request.user == listing.user:
        messages.error(request, 'You cannot bid on your own listing.')
        return
    if x == 'update_bid' and bid_now < float(request.POST['bid']):
        bid_to_be_updated = listing.bid
        bid_to_be_updated.highest_bidder = User.objects.get(username=request.user)
        bid_to_be_updated.current_bid = float(request.POST['bid'])
        bid_to_be_updated.number_of_bids += 1
        bid_to_be_updated.save()

    elif x == 'new_bid' and bid_now < float(request.POST['bid']):
        Bid.objects.create(listing=listing, highest_bidder=User.objects.get(username=request.user),
                           number_of_bids=1, current_bid=float(request.POST['bid']))

    else:
        messages.error(request, 'Your bid is less than or equal to current bid.')


def comment_handler(listing_id, request):
    listing = Listings.objects.get(pk=listing_id)
    Comment.objects.create(listing=listing, commenter=User.objects.get(username=request.user),
                           description=request.POST['comment'])


@login_required
def watchlist(request):
    print(request.POST)
    if request.method == "POST" and request.POST.get('watchlist-button', '') == "add":
        listing = Listings.objects.get(pk=int(request.POST['listing_id']))
        Watchlist.objects.create(listing=listing, user=User.objects.get(username=request.user))
        return HttpResponseRedirect(reverse('listingdetail', kwargs={'listing_id': listing.id}))
    elif request.method == "POST" and request.POST.get('watchlist-button', '') == "remove":
        listing = Listings.objects.get(pk=int(request.POST['listing_id']))
        watchlist = Watchlist.objects.get(listing=listing, user=User.objects.get(username=request.user))
        watchlist.delete()
        return HttpResponseRedirect(reverse('listingdetail', kwargs={'listing_id': listing.id}))

    # GET REQUEST region
    context = {
        'all_watchlists': Watchlist.objects.filter(user=User.objects.get(username=request.user)).order_by('-id')
    }
    return render(request, 'auctions/watchlist.html', context)


def category(request, category_name):
    if category_name == 'all':
        context = {
            'categories': set([listing.category for listing in Listings.objects.filter(status='active')])
        }

        return render(request, 'auctions/category_listings.html', context)
    elif category_name in [i[0] for i in Listings.CATEGORY]:
        category_wise_listings = Listings.objects.filter(category=category_name, status='active').order_by('-id')
        context = {
            'listings': category_wise_listings,
            'is_category': True,
            'category_name': category_name
        }
        return render(request, "auctions/index.html", context)

    return HttpResponse(f"<h2>This {category_name} is not a valid category</h2>")

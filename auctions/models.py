from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass


class Listings(models.Model):
    CATEGORY = (
        ('FASHION', 'FASHION'),
        ('HOME', 'HOME'),
        ('ELECTRONICS', 'ELECTRONICS'),
        ('SPORTS', 'SPORTS'),
        ('HEALTH AND BEAUTY', 'HEALTH AND BEAUTY'),
        ('TOYS OR BABY ITEMS', 'TOYS OR BABY ITEMS'),
        ('VEHICLE PARTS AND MOTORS', 'VEHICLE PARTS AND MOTORS'),
        ('OTHERS', 'OTHERS')
    )
    title = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    initial_bid = models.FloatField(verbose_name='Initial Bid', default=0)
    category = models.CharField(max_length=30, choices=CATEGORY, default='OTHERS', blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    image = models.TextField(blank=True)
    status = models.CharField(max_length=10, default='active')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='listings')

    def __str__(self):
        return f"{self.id}-{self.title} - {self.initial_bid}"


class Bid(models.Model):
    listing = models.OneToOneField(Listings, on_delete=models.CASCADE, related_name='bid')
    highest_bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='highest_bidder')
    number_of_bids = models.IntegerField(default=0)
    current_bid = models.FloatField()

    def __str__(self):
        return f"{self.listing.title}-{self.highest_bidder}-{self.current_bid}"


class Comment(models.Model):
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name='comment')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
    description = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}-{self.commenter.username}"


class Watchlist(models.Model):
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name='watchlists')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='all_watchlists')

    def __str__(self):
        return f"{self.listing.title}-{self.user.username}"

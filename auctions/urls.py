from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
                  path("", views.index, name="index"),
                  path("login", views.login_view, name="login"),
                  path("logout", views.logout_view, name="logout"),
                  path("register", views.register, name="register"),
                  path('create', views.createlistings, name='createlistings'),
                  path('listings/<int:listing_id>', views.listing_detail, name="listingdetail"),
                  path('watchlist', views.watchlist, name='watchlist'),
                  path('category/<str:category_name>', views.category, name='category'),
                  path('closed_listings', views.closed_listings_view, name="closedlistings")

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

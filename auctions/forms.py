from .models import *
from django.forms import ModelForm


class ListingForm(ModelForm):
    class Meta:
        model = Listings
        fields = ['title', 'description', 'initial_bid', 'category', 'image']



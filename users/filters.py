from cProfile import Profile
from random import choices
import django_filters

from .models import ProfileModel

class ListingFilter(django_filters.FilterSet):

    class Meta:
        model = ProfileModel
        fields = {'name': {'icontains'}}

class StoryFilter(django_filters.FilterSet):
    
    class Meta:
        model = ProfileModel
        fields = {'name':{'icontains'}}
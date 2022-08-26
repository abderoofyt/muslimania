from random import choices
import django_filters

from .models import ProfileModel
from stories.models import Book

class ListingFilter(django_filters.FilterSet):

    class Meta:
        model = ProfileModel
        fields = {'name': {'icontains'}, 'sex':{'exact'}}

class StoryFilter(django_filters.FilterSet):
    
    class Meta:
        model = ProfileModel
        fields = {'name':{'icontains'}}


class BookFilter(django_filters.FilterSet):
    
    class Meta:
        model = Book
        fields = {'about':{'icontains'}}
from django import forms
from .models import Book, Publisher

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [f.name for f in Book._meta.fields]

class PublisherCreateForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = [f.name for f in Publisher._meta.fields]
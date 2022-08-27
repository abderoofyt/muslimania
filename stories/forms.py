from django import forms
from .models import Book, Publisher

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [f.name for f in Book._meta.fields]

class CreatePublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = [f.name for f in Publisher._meta.fields]
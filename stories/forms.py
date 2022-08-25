from django import forms
from .models import BookModel, Publisher

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = [f.name for f in BookModel._meta.fields]

class PublisherCreateForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = [f.name for f in Publisher._meta.fields]
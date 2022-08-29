from django import forms
from .models import Author, Book, Publisher, Story

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class CreatePublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'

class CreateChapterForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = '__all__'

class AuthorCreateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
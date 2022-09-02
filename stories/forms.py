from django import forms
from .models import Author, Book, Chapter, Publisher, Story, Comment

class StoryForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')

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

class ChapterCreateForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = '__all__'

class AuthorCreateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class EditStoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = '__all__'
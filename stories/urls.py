from django.urls import path
from .views import PublisherListView, PublisherBookListView, AuthorDetailView, BookDetailView
from . import views

urlpatterns = [
    path('publishers/', PublisherListView.as_view(), name="publishers"),
    path('books/<publisher>/', PublisherBookListView.as_view(), name="book_by"),

    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
]
from django.urls import path
from .views import PublisherListView, PublisherBookListView, AuthorDetailView, BookDetailView, BooksListView, StoriesListView
from . import views

urlpatterns = [
    path('stories/', StoriesListView.as_view(), name="stories"),
    path('books/', BooksListView.as_view(), name="books"),
    path('publishers/', PublisherListView.as_view(), name="publishers"),
    
    
    path('books/<publisher>/', PublisherBookListView.as_view(), name="book_by"),

    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),

    path('publisher/create/', views.publisher_create_view, name="publisher_create_view"),
    path('book/create/', views.book_create_view, name="book_create_view"),
]
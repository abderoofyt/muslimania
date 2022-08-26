from django.urls import path
from .views import PublisherListView, PublisherBookListView, AuthorDetailView, BookDetailView, BooksListView
from . import views

urlpatterns = [
    path('books/', BooksListView.as_view(), name="books"),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', views.book_create_view, name="book_create_view"),
    
    path('books/publishers/<publisher>/', PublisherBookListView.as_view(), name="book_by"),

    path('publishers/', PublisherListView.as_view(), name="publishers"),
    path('publishers/create/', views.publisher_create_view, name="publisher_create_view"),
   
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    
]
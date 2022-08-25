from django.views.generic import ListView, DetailView
from .models import Publisher, Book, Author

from django.shortcuts import get_object_or_404, render
from django.utils import timezone
import uuid

class PublisherListView(ListView):
    model = Publisher
    context_object_name = 'my_favorite_publishers'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context

class PublisherBookListView(ListView):
    
    template_name = 'stories/books_by_publisher.html'
    paginate_by = 2

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
        return Book.objects.filter(publisher=self.publisher)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['publisher'] = self.publisher
        return context


class BookListView(ListView):
    queryset = Book.objects.order_by('-publication_date')
    context_object_name = 'book_list'
    

class AcmeBookListView(ListView):
    
    context_object_name = 'book_list'
    queryset = Book.objects.filter(publisher__name='ACME Publishing')
    template_name = 'stories/acme_list.html'


class PublisherDetailView(DetailView):
    
    context_object_name = 'publisher'
    queryset = Publisher.objects.all()

class BookDetailView(DetailView):
    model = Book
    template_name = 'stories/book_view.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BookDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.filter(pk=self.kwargs.get('pk'))
        return context

class AuthorDetailView(DetailView):
    
    queryset = Author.objects.all()

    def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.last_accessed = timezone.now()
        obj.save()
        return obj
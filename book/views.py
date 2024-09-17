from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.views.generic import ListView, DetailView
from .models import Book, BookRepository
from .forms import BookForm


class BookListView(ListView):
    template_name = 'book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        books = BookRepository(Book)
        return books.get_books()


class BookDetailView(DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book'

    def get_queryset(self):
        book = BookRepository(Book)
        return book.get_by_id(self.kwargs['pk'])
    

# class AddBookView(FormView):
#     template_name = 'book_form.html'
#     form_class = BookForm
#     success_url = '/book'

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

class AddBookView(CreateView):
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = '/book'


    def get_queryset(self):
        books = BookRepository(Book)
        return books.get_books()
 

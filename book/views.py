from django.shortcuts import render
from django.utils import timezone
from django.views.generic.list import ListView
from .models import Book


def BooksOnTheTable(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books':books})

class BookListView(ListView):
    model = Book
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context

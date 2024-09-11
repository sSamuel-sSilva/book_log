from django.urls import path, include
from .views import BookListView, BooksOnTheTable

urlpatterns = [
    path("", BooksOnTheTable, name='books'),
    path('book/', BookListView.as_view(), name='book-list-view'),    
]
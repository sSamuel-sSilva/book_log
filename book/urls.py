from django.urls import path, include
from .views import BookListView, BookDetailView, AddBookView, UpdateBookView

urlpatterns = [
    path('', BookListView.as_view(), name='book-list-view'), 
    path('<int:pk>', BookDetailView.as_view(), name='book-detail-view'),
    path('<int:pk>/update', UpdateBookView.as_view(), name='book-update-view'),
    path('add', AddBookView.as_view(), name='book-create'), 
]
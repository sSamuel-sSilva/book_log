from django.urls import path, include
from .views import BookListView, BookDetailView, AddBookView

urlpatterns = [
    path('', BookListView.as_view(), name='book-list-view'), 
    path('<int:pk>', BookDetailView.as_view(), name='book-detail-view'),
    path('add', AddBookView.as_view(), name='book-create'), 
]
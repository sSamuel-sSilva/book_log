from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.FloatField()
    date_pub = models.DateField()                        


    def get_absolute_url(self):
        return reverse('book-detail-view', kwargs={'pk': self.pk})


    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ['title']

        
    
class BookRepository(models.Model):
    def get_books(self):
        return Book.objects.all()


    def get_by_id(self, id):
        return Book.objects.filter(id=id)
    

    def get_by_author(self, author):
        return Book.objects.filter(author=author)
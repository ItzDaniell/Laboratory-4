from django.db import models
from library.models import Book, Author, Category, Publisher
from users.models import LibraryUser

class BookView(models.Model):
    """Model to track book page views"""
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='views')
    user = models.ForeignKey(LibraryUser, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"View of {self.book.title}"

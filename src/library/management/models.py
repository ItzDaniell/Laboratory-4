from django.db import models
from library.models import Book, Publisher
from users.models import LibraryUser

class LibraryBranch(models.Model):
    """Model for physical library locations"""
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    opening_hours = models.TextField()
    
    def __str__(self):
        return self.name


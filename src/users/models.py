from django.db import models
from django.contrib.auth.models import AbstractUser
from library.models import Book, Category

class LibraryUser(AbstractUser):
    """Extended user model with additional library-related fields"""
    bio = models.TextField(blank=True)
    favorite_categories = models.ManyToManyField(Category, blank=True, related_name='fans')
    profile_image = models.ImageField(upload_to='user_profiles/', blank=True)

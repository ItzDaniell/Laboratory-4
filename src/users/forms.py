from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import LibraryUser

class LibraryUserCreationForm(UserCreationForm):
    class Meta:
        model = LibraryUser
        fields = ['username']

class LibraryUserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Usuario', max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
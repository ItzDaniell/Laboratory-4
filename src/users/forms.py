from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import LibraryUser, ReadingList

class LibraryUserCreationForm(UserCreationForm):
    class Meta:
        model = LibraryUser
        fields = ['username']

class LibraryUserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Usuario', max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
class ReadingListForm(forms.ModelForm):
    """Formulario para crear o editar listas de lectura"""
    class Meta:
        model = ReadingList
        fields = ['name', 'description', 'books', 'is_public']
        widgets = {
            'books': forms.CheckboxSelectMultiple(),
        }
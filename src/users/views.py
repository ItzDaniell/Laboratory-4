from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import LibraryUserCreationForm

def register(request):
    if request.method == 'POST':
        form = LibraryUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = LibraryUserCreationForm()

    return render(request, 'users/register.html', {'form': form})
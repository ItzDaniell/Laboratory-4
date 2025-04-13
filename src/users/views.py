from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import LibraryUserCreationForm, ReadingListForm
from django.contrib.auth.decorators import login_required
from .models import ReadingList

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

@login_required
def all_reading_list(request):
    reading_lists = ReadingList.objects.filter(is_public=True).order_by('-created_at')
    return render(request, 'users/all_reading_list.html', {'reading_lists': reading_lists})

@login_required
def create_reading_list(request):
    """Vista para crear una nueva lista de lectura"""
    if request.method == 'POST':
        form = ReadingListForm(request.POST)
        if form.is_valid():
            reading_list = form.save(commit=False)
            reading_list.user = request.user
            reading_list.save()
            return redirect('home')
    else:
        form = ReadingListForm()
    return render(request, 'users/create_reading_list.html', {'form': form})
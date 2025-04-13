from django.shortcuts import render, get_object_or_404
from .models import BookView, CategoryAnalytics, AuthorAnalytics, RecommendationLog
from library.models import Book
from users.models import LibraryUser

def book_views(request):
    views = BookView.objects.select_related('book', 'user').order_by('-timestamp')
    return render(request, 'analytics/book_views.html', {'views': views})

def category_analytics(request):
    categories = CategoryAnalytics.objects.select_related('category')
    return render(request, 'analytics/category_analytics.html', {'categories': categories})

def author_analytics(request):
    authors = AuthorAnalytics.objects.select_related('author')
    return render(request, 'analytics/author_analytics.html', {'authors': authors})

def user_recommendations(request, user_id):
    user = get_object_or_404(LibraryUser, id=user_id)
    recommendations = RecommendationLog.objects.filter(user=user).select_related('book')
    return render(request, 'analytics/user_recommendations.html', {
        'user': user,
        'recommendations': recommendations
    })
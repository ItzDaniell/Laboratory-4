from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('reading-lists/', views.all_reading_list, name='all_reading_list'),
    path('reading-list/create/', views.create_reading_list, name='create_reading_list'),

]
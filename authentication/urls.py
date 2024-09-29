from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Register URL
    path('register/', views.register, name='register'),
    # Login URL (using built-in Django LoginView)
    path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html'), name='login'),
    # Logout URL
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]

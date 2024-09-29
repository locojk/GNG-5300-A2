from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),  # List all students
    path('<int:pk>/', views.student_detail, name='student_detail'),  # View a student's details
    path('new/', views.student_create, name='student_create'),  # Add a new student
    path('<int:pk>/edit/', views.student_edit, name='student_edit'),  # Edit a student's details
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
]


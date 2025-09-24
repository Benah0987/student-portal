from django.urls import path
from school import views

urlpatterns = [
    path('', views.index, name='index'),

    # Student
    path('dashboard/', views.dashboard, name='dashboard'),

    # Teacher
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),

    # Admin
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
]

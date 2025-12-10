from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Student
    path('dashboard/', views.dashboard, name='dashboard'),

    # Teacher
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),

    # Admin
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('notification/mark-as-read/', views.mark_notification_as_read, name='mark_notification_as_read' ),
   path('notification/clear-all', views.clear_all_notification, name= "clear_all_notification")

]

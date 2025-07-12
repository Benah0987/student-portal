from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
     path('add-student/', views.add_student, name='add-student'),
    path('add-student/', views.add_student, name='add-student'),
    path('edit-student/', views.edit_student, name='edit-student'),
    path('student-details/', views.view_student, name='view-student'),
]

from django.contrib import admin
from django.urls import path
from school import views  # ✅ import views from your app

urlpatterns = [
    path('', views.index, name='index'),  # ✅ corrected syntax
]

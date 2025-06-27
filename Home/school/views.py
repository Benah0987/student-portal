from django.shortcuts import render
from django.http import HttpResponse  # ✅ Import this

# Create your views here.

def index(request):  # ✅ Use 'request' instead of 'report'
    return HttpResponse("Hello world")

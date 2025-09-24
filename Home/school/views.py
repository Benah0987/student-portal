from django.shortcuts import render

def index(request):
    return render(request, "Home/index.html")

def dashboard(request):  # Student dashboard
    return render(request, "students/student-dashboard.html")

def teacher_dashboard(request):  # Teacher dashboard
    return render(request, "teachers/teacher-dashboard.html")

def admin_dashboard(request):  # Admin dashboard
    return render(request, "admins/admin-dashboard.html")

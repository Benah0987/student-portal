from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "Home/index.html")


def dashboard(request):  # Student dashboard
    user = request.user
    if not user.is_student:
        return redirect('login')  # prevent non-students from viewing
    return render(request, "students/student-dashboard.html", {'user': user})


def teacher_dashboard(request):  # Teacher dashboard
    user = request.user
    if not user.is_teacher:
        return redirect('login')
    return render(request, "teachers/teacher-dashboard.html", {'user': user})


def admin_dashboard(request):  # Admin dashboard
    user = request.user
    if not user.is_admin:
        return redirect('login')
    return render(request, "admins/admin-dashboard.html", {'user': user})

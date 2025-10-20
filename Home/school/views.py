from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required

from .models import Notification  # ✅ Correct import — no circular import


def index(request):
    return render(request, "Home/index.html")


def dashboard(request):
    unread_notification = Notification.objects.filter(user=request.user, is_read=False)
    unread_notification_count = unread_notification.count()
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

def mark_notification_as_read(request):
    if request.method == 'POST':
        notification = Notification.objects.filter(user=request.user, is_read=False)
        notification.update(is_read=True)
        return JsonResponse({'status': 'success'})
    return HttpResponseForbidden()

def clear_all_notification(request):
    if request.method == "POST":
        notification = Notification.objects.filter(user=request.user)
        notification.delete()
        return JsonResponse({'status': 'success'})
    return HttpResponseForbidden
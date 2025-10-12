from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser, PasswordResetRequest
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST.get('role')  # 'student', 'teacher', or 'admin'

        # ✅ Use email for creation (no username field anymore)
        user = CustomUser.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        # Assign roles
        user.is_student = role == 'student'
        user.is_teacher = role == 'teacher'
        user.is_admin = role == 'admin'
        user.save()

        messages.success(request, 'Signup successful! You can now log in.')
        return redirect('login')

    return render(request, 'authentication/register.html')


def login_view(request):
    # ✅ If user already logged in, redirect based on role
    if request.user.is_authenticated:
        if request.user.is_admin:
            return redirect('admin_dashboard')
        elif request.user.is_teacher:
            return redirect('teacher_dashboard')
        elif request.user.is_student:
            return redirect('dashboard')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # ✅ Use email (not username)
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')

            # Redirect based on role
            if user.is_admin:
                return redirect('admin_dashboard')
            elif user.is_teacher:
                return redirect('teacher_dashboard')
            elif user.is_student:
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid user role.')
                return redirect('index')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')

    return render(request, 'authentication/login.html')


def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = CustomUser.objects.filter(email=email).first()
        
        if user:
            # Generate a unique token
            token = get_random_string(50)
            reset_request = PasswordResetRequest.objects.create(
                user=user,
                email=email,
                token=token
            )

            # Construct the reset link
            reset_link = f"http://127.0.0.1:8000/authentication/reset-password/{token}/"

            # Email content
            subject = "Password Reset Request"
            message = (
                f"Hello {user.first_name or 'User'},\n\n"
                f"We received a request to reset your password.\n"
                f"Click the link below to reset it:\n{reset_link}\n\n"
                f"If you didn’t request this, please ignore this email.\n\n"
                f"Best regards,\nStudent Portal Support"
            )

            try:
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email],
                    fail_silently=False,
                )
                messages.success(request, "A password reset link has been sent to your email.")
            except Exception as e:
                print(f"Email send error: {e}")
                messages.error(request, "There was an error sending the email. Please try again.")
        else:
            messages.error(request, "No account found with that email address.")
    
    return render(request, 'authentication/forgot-password.html')


def reset_password_view(request, token):
    reset_request = PasswordResetRequest.objects.filter(token=token).first()
    
    if not reset_request or not reset_request.is_valid():
        messages.error(request, 'Invalid or expired reset link')
        return redirect('index')

    if request.method == 'POST':
        new_password = request.POST['new_password']
        reset_request.user.set_password(new_password)
        reset_request.user.save()
        messages.success(request, 'Password reset successful')
        return redirect('login')

    return render(request, 'authentication/reset_password.html', {'token': token})


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('index')

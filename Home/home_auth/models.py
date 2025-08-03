from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings


class CustomUser(AbstractUser):
    is_authorized = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='customuser_set'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='customuser_set'
    )

    def __str__(self):
        return self.username


class PasswordResetRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField()
    token = models.CharField(max_length=32, default=get_random_string, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reset Request for {self.email}"

    def send_reset_email(self):
        reset_link = f"http://localhost:8000/reset-password/{self.token}/"
        send_mail(
            'Password Reset Request',
            f'Click the following link to reset your password: {reset_link}',
            settings.DEFAULT_FROM_EMAIL,
            [self.email],
            fail_silently=False,
        )

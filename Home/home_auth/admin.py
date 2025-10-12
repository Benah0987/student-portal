from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser


class CustomUserAdmin(DefaultUserAdmin):
    model = CustomUser
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'is_student', 'is_teacher', 'is_admin', 'is_active')
    list_filter = ('is_student', 'is_teacher', 'is_admin', 'is_active', 'is_staff', 'is_superuser')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Roles'), {'fields': ('is_student', 'is_teacher', 'is_admin')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_authorized', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2',
                       'is_student', 'is_teacher', 'is_admin', 'is_active')}
        ),
    )

    search_fields = ('email', 'first_name', 'last_name')


admin.site.register(CustomUser, CustomUserAdmin)

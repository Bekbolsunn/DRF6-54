from django.contrib import admin
from users.models import CustomUser
from django.contrib.auth.admin import UserAdmin


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ("id", "email")
    fieldsets = (
        (None, {"fields": ("email", "password", "is_active")}),
        ("Important dates", {"fields": ("last_login",)}),
    )
    ordering = ("last_login",)
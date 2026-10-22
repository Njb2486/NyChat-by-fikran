from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class NyChatUserAdmin(UserAdmin):
    ordering = ("email",)
    list_display = ("email", "display_name", "role", "is_active", "is_email_verified")
    list_filter = ("role", "is_active", "is_email_verified", "is_phone_verified")
    search_fields = ("email", "display_name", "phone_number")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Profile", {"fields": ("display_name", "phone_number", "role", "is_private")}),
        ("Verification", {"fields": ("is_email_verified", "is_phone_verified")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = ((None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),)
    filter_horizontal = ("groups", "user_permissions")

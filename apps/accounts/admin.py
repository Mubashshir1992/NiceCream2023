from django.contrib import admin
from django.contrib.auth.admin import Group, UserAdmin
from .forms import CustomUserCreateonForm, CustomUserChangrForm
from .models import User
# Register your models here.
admin.site.unregister(Group)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreateonForm
    form = CustomUserChangrForm
    model = User
    list_display = ['username', 'phone', 'balance', 'address', 'is_active', 'is_staff', 'is_superuser']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone',)}),
        (None, {'fields': ('image',)}),
        (None, {'fields': ('address',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone','first_name', 'last_name', 'email', 'activated_date', 'image', 'address',)}),
    )

admin.site.register(User, CustomUserAdmin)
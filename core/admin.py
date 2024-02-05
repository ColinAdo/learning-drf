from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationsForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationsForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'age', 'is_active', 'is_staff']

    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('age', )}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('age', )}),)

admin.site.register(CustomUser, CustomUserAdmin)

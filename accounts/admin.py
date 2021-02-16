from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth.models import Group


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('username', 'last_name', 'is_active', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('Main', {'fields':('username', 'first_name', 'last_name', 'password')}),
        ('Personal Info', {'fields': ('email', 'phone', 'image', 'start_time', 'login_time')}),
        ('Permissions', {'fields': ('is_active', 'is_admin')})
    )
    add_fieldsets = (
        (None, {
            # 'fields': ('username', 'password', 're_password', 'first_name', 'last_name', 'email', 'phone')
            'fields': ('username', 'password', 're_password', 'last_name', 'phone')
        }),
    )
    readonly_fields = ('start_time', 'login_time')
    search_fields = ('username', 'first_name', 'last_name')
    ordering = ('username', 'last_name')
    filter_horizontal = ()

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
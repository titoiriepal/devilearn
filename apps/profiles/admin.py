from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, InstructorProfile
# Register your models here.


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + \
        (('Custom Role', {'fields': ('is_instructor',)}),)
    add_fieldsets = BaseUserAdmin.add_fieldsets + \
        ((None, {'fields': ('is_instructor',)}),)
    # list_display = ('username', 'email', 'is_instructor', 'is_staff')
    # search_fields = ('username', 'email')
    # list_filter = ('is_instructor', 'is_staff')


admin.site.register(InstructorProfile)

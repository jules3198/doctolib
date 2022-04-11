from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.


from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff'
        )
    pass

admin.site.register(CustomUser, CustomUserAdmin)
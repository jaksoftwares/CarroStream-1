from django.contrib import admin
from .models import User  # Import your custom User model

# Register the User model with Django Admin
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'full_name', 'email', 'is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'full_name')
    list_filter = ('is_active', 'is_staff')
    ordering = ('-date_joined',)
    
# Register the custom user model with the admin site
admin.site.register(User, UserAdmin)

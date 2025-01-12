from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at', 'updated_at', 'price']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Service, ServiceAdmin)
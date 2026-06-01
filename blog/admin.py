from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

admin.site.register(Blog, BlogAdmin)
from django.contrib import admin
from .models import Task




@admin.register(Task)
class TasksAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'status', 'created_at', 'updated_at']  # Fields to display
    search_fields = ['title', 'description']  # Enable search by title and description
    list_per_page = 20  # Number of items per page

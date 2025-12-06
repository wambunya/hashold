from django.contrib import admin
from .models import Project, BlogPost, Booking

# Configure the Admin Interface
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)

@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_published', 'is_featured')
    list_filter = ('is_featured', 'category')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    list_editable = ('status',)  # Allows you to change status directly from the list view
    search_fields = ('name', 'email')
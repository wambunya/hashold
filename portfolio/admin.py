from django.contrib import admin
from .models import Project, ProjectImage, BlogPost, Booking

# This allows uploading multiple images inside the Project page
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3  # <--- Shows 3 empty upload slots by default (you can click 'Add another' for more)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_type', 'category', 'created_at')
    list_filter = ('project_type', 'category')
    search_fields = ('title',)
    
    # This line connects the images to the project page
    inlines = [ProjectImageInline]

@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_published', 'is_featured')
    list_filter = ('is_featured', 'category')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'status', 'created_at')
    list_editable = ('status',)
    list_filter = ('status',)
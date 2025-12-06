from django.db import models

class Project(models.Model):
    # 1. Project Type Selection
    PROJECT_TYPES = [
        ('WEB', 'Web Development'),
        ('DESIGN', 'Graphic Design'),
    ]
    
    # 2. Categories
    CATEGORY_CHOICES = [
        ('BRANDING', 'Branding'),
        ('UIUX', 'UI/UX Design'),
        ('ECOMMERCE', 'E-Commerce'),
        ('WEB_DEV', 'Website Development'),
        ('PRINT', 'Print & Packaging'),
        ('SOCIAL', 'Social Media'),
    ]
    
    title = models.CharField(max_length=200)
    project_type = models.CharField(max_length=10, choices=PROJECT_TYPES, default='WEB')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    color_class = models.CharField(max_length=50, default='bg-slate-900', help_text="Tailwind class like 'bg-amber-900'")
    
    # Cover Image (Shown on the main work page)
    image = models.ImageField(upload_to='projects/covers/', blank=True, null=True)
    description = models.TextField()
    
    # Link for Web Projects
    live_link = models.URLField(blank=True, null=True, help_text="Required for Web Development projects")
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='gallery_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/gallery/')
    
    def __str__(self):
        return f"Image for {self.project.title}"

# --- RESTORED CLASSES BELOW ---

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    excerpt = models.TextField()
    content = models.TextField()
    read_time = models.CharField(max_length=20, default="5 min read")
    date_published = models.DateField()
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending Payment'),
        ('PAID', 'Paid'),
        ('IN_PROGRESS', 'In Progress'),
        ('DELIVERED', 'Delivered'),
        ('FINISHED', 'Finished'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    project_details = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.get_status_display()}"
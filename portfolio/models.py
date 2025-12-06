from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('BRANDING', 'Branding'),
        ('ILLUSTRATION', 'Illustration'),
        ('WEB DESIGN', 'Web Design'),
        ('PRINT', 'Print Design'),
    ]
    
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    # We use a color field to match your design's gradient backgrounds
    color_class = models.CharField(max_length=50, default='bg-gray-900', help_text="Tailwind class like 'bg-amber-900'")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

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
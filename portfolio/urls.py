from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('work/', views.work, name='work'),
    path('work/<int:pk>/', views.project_detail, name='project_detail'), # Detail page for Design Projects
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'), # Detail page for Blog Posts
    path('resources/', views.resources, name='resources'),
    path('contact/', views.contact, name='contact'),
]
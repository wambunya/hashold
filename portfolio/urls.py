from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('work/', views.work, name='work'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('resources/', views.resources, name='resources'),
    path('contact/', views.contact, name='contact'),
]
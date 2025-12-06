from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Project, BlogPost, Booking

def home(request):
    expertise = [
        {'title': 'BRANDING', 'desc': 'Creating memorable identities that resonate with your audience and stand the test of time.'},
        {'title': 'ILLUSTRATION', 'desc': 'Custom artwork that tells your story with personality, creativity, and visual impact.'},
        {'title': 'WEB DESIGN', 'desc': 'Beautiful, functional websites that engage users and elevate your digital presence.'},
        {'title': 'PRINT DESIGN', 'desc': 'From business cards to banners, print materials that make a lasting impression.'},
        {'title': 'GRAPHIC DESIGN', 'desc': 'Visual solutions that communicate clearly and captivate effectively across all media.'},
        {'title': 'EVENT MATERIALS', 'desc': 'Eye-catching backdrops, roll-ups, and signage that transform spaces and events.'}
    ]
    return render(request, 'portfolio/home.html', {'page': 'home', 'expertise': expertise})

def about(request):
    return render(request, 'portfolio/about.html', {'page': 'about'})

def work(request):
    # Fetch projects from Database
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'portfolio/work.html', {'page': 'work', 'projects': projects})

def blog(request):
    # Fetch blog posts from Database
    posts = BlogPost.objects.all().order_by('-date_published')
    return render(request, 'portfolio/blog.html', {'page': 'blog', 'posts': posts})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_content = request.POST.get('message')

        # 1. Save to Database
        booking = Booking.objects.create(
            name=name,
            email=email,
            project_details=message_content
        )

        # 2. Send Email Notification
        subject = f"New Project Inquiry from {name}"
        message = f"Client: {name}\nEmail: {email}\n\nDetails:\n{message_content}"
        
        try:
            send_mail(
                subject,
                message,
                'system@creativehub.com', # From
                ['your-email@gmail.com'], # To (Replace with your email)
                fail_silently=False,
            )
            messages.success(request, 'Message sent successfully! We will contact you shortly.')
            
            # WhatsApp Note: 
            # To send WhatsApp, you would typically use an API like Twilio here.
            # Example pseudocode: 
            # client.messages.create(body=message, from_='whatsapp:+14155238886', to='whatsapp:+254700000000')

        except Exception as e:
            messages.error(request, 'Error sending message. Please try again.')

        return redirect('contact')

    return render(request, 'portfolio/contact.html', {'page': 'contact'})

# ... (Add services and resources views as defined previously)
def services(request):
     # You can also make Services a model if you want them editable
    services_list = [
        {'title': 'BRAND IDENTITY', 'description': '...', 'includes': ['Logo', 'Strategy']},
    ]
    return render(request, 'portfolio/services.html', {'page': 'services', 'services': services_list})

def resources(request):
    return render(request, 'portfolio/resources.html', {'page': 'resources'})
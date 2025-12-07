from django.shortcuts import render, redirect, get_object_or_404
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
    # Fetch all projects ordered by newest first
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'portfolio/work.html', {'page': 'work', 'projects': projects})

def project_detail(request, pk):
    # This is the view for the Design Gallery Page
    project = get_object_or_404(Project, pk=pk)
    
    # If it's a web project, redirect to the live link as a fail-safe
    if project.project_type == 'WEB' and project.live_link:
        return redirect(project.live_link)
        
    return render(request, 'portfolio/project_detail.html', {'project': project})

def services(request):
    services_list = [
        {
            'title': 'BRAND IDENTITY',
            'description': 'Complete brand development from concept to execution, including logo design, color palettes, typography systems, and brand guidelines.',
            'includes': ['Logo Design', 'Brand Strategy', 'Style Guides', 'Brand Collateral']
        },
        {
            'title': 'GRAPHIC DESIGN',
            'description': 'Creative visual solutions for all your marketing and communication needs, crafted to engage and inspire your audience.',
            'includes': ['Marketing Materials', 'Social Media Graphics', 'Infographics', 'Presentation Design']
        },
        {
            'title': 'ILLUSTRATION',
            'description': 'Custom illustrations that bring personality and uniqueness to your brand, from character design to editorial illustrations.',
            'includes': ['Digital Illustration', 'Character Design', 'Icon Sets', 'Editorial Art']
        },
        {
            'title': 'WEB DESIGN',
            'description': 'User-centered web design that combines aesthetics with functionality, creating seamless digital experiences.',
            'includes': ['Website Design', 'Landing Pages', 'UI/UX Design', 'Responsive Design']
        },
        {
            'title': 'PRINT SERVICES',
            'description': 'Professional print design for all formats, ensuring your materials look stunning in physical form.',
            'includes': ['Business Cards', 'Brochures', 'Flyers', 'Posters', 'Magazines']
        },
        {
            'title': 'EVENT MATERIALS',
            'description': 'Large-format designs that transform spaces and create memorable event experiences.',
            'includes': ['Roll-up Banners', 'Event Backdrops', 'T-shirt Design', 'Signage', 'Stage Graphics']
        }
    ]
    return render(request, 'portfolio/services.html', {'page': 'services', 'services': services_list})

def blog(request):
    # Fetch all blog posts ordered by newest first
    posts = BlogPost.objects.all().order_by('-date_published')
    return render(request, 'portfolio/blog.html', {'page': 'blog', 'posts': posts})

def blog_detail(request, pk):
    # This is the NEW view for the single Blog Post Page
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'portfolio/blog_detail.html', {'post': post})

def resources(request):
    resources_list = [
         {'title': 'The Ultimate Branding Checklist', 'type': 'DOWNLOAD', 'desc': 'Essential steps to build a memorable brand identity'},
         {'title': 'Color Psychology in Design', 'type': 'ARTICLE', 'desc': 'Understanding how colors influence emotions and decisions'},
         {'title': 'Typography Best Practices', 'type': 'GUIDE', 'desc': 'Master the art of selecting and pairing fonts effectively'},
         {'title': 'Free Design Templates', 'type': 'DOWNLOAD', 'desc': 'Customizable templates for social media and print'},
         {'title': 'Print Design Specifications', 'type': 'GUIDE', 'desc': 'Technical requirements for flawless print production'},
         {'title': 'Logo Design Process Revealed', 'type': 'ARTICLE', 'desc': 'Behind-the-scenes look at creating iconic logos'}
    ]
    return render(request, 'portfolio/resources.html', {'page': 'resources', 'resources': resources_list})

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
                'system@wambunya.com', 
                ['wambunyahashold@gmail.com'], 
                fail_silently=False,
            )
            messages.success(request, 'Message sent successfully! We will contact you shortly.')

        except Exception as e:
            # For development, it's useful to print the error to console
            print(e)
            messages.error(request, 'Error sending message. Please try again.')

        return redirect('contact')

    return render(request, 'portfolio/contact.html', {'page': 'contact'})

def solutions(request):
    return render(request, 'portfolio/solutions.html')

def integration(request):
    return render(request, 'portfolio/integration.html')

def privacy(request):
    return render(request, 'portfolio/privacy.html')

def terms(request):
    return render(request, 'portfolio/terms.html')
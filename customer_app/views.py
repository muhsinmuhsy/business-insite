from django.shortcuts import render
from admin_app.models import Service
# Create your views here.

def home(request):
    current_page = 'home'
    context = {
        'current_page': current_page
    }
    return render(request, 'customer_app/pages/home.html', context)

def about(request):
    current_page = 'about'
    context = {
        'current_page': current_page
    }
    return render(request, 'customer_app/pages/about.html', context)

def services(request):
    current_page = 'services'
    services = Service.objects.all().order_by('-id')

    chunk_size = 4
    services_chunks = [services[i:i + chunk_size] for i in range(0, len(services), chunk_size)]

    context = {
        'current_page': current_page,
        'services': services,
        'services_chunks': services_chunks,
    }
    return render(request, 'customer_app/pages/services.html', context)


def contact(request):
    current_page = 'contact'
    context = {
        'current_page':current_page
    }
    return render(request, 'customer_app/pages/contact.html', context)

def services_details(request):
    current_page = 'services_details'
    context = {
        'current_page': current_page
    }
    return render(request, 'customer_app/pages/services_details.html', context)
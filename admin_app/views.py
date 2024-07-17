from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Service
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/admin/login/')
def dashboard(request):
    current_page = 'dashboard'
    services_count = Service.objects.count()
    context = {
        'current_page': current_page,
        'services_count': services_count,
        }
    return render(request, 'admin_app/pages/dashboard.html', context)


def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error = 'User Name or Password Incorrect.'
    else:
        error = None
    return render(request, 'admin_app/pages/login.html', {'error': error})

@login_required(login_url='/admin/login/')
def logout_view(request):
    logout(request)
    return redirect('index')

@login_required(login_url='/admin/login/')
def service_list(request):
    current_page = 'service_list'
    services = Service.objects.all()
    context = {
        'current_page': current_page,
        'services': services
        }
    return render(request, 'admin_app/pages/service_list.html', context)

# @login_required(login_url='/admin/login/')
# def service_view(request, service_id):
#     current_page = 'service_view'
#     try:
#         service = Service.objects.get(id=service_id)
#     except Service.DoesNotExist:
#         messages.error(request, 'service not found')
#         return redirect('service_list')
#     context = {
#         'current_page': current_page,
#         'service':service
#     }
#     return render(request, 'admin_app/pages/service_view.html', context)

@login_required(login_url='/admin/login/')
def service_add(request):
    current_page = 'service_add'
    if request.method == 'POST':
        image = request.FILES.get('image') 
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        try:
            service = Service(
                image=image,
                title=title,
                description=description,
            )
            service.save()
            messages.success(request, 'service added successfully')
            return redirect('service_list')
        except Exception as e:
            messages.error(request, f'Error adding service: {e}')
            return redirect('service_add')
        
    context = {
        'current_page': current_page,
    } 
    return render(request, 'admin_app/pages/service_add.html', context)

@login_required(login_url='/admin/login/')
def service_edit(request, service_id):
    current_page = 'service_edit'
    try:
        service = Service.objects.get(id=service_id)
    except Service.DoesNotExist:
        messages.error(request, 'service not found')
        return redirect('service_list')

    if request.method == 'POST':
        try:
            image = request.FILES.get('image')
            service.title = request.POST.get('title')
            service.description = request.POST.get('description')
            
            if image:
                service.image = image

            service.save()
            messages.success(request, 'service edited successfully')
            return redirect('service_list')
        except Exception as e:
            messages.error(request, f'Error editing service: {e}')
            return redirect('service_edit', service_id=service.id) 

    context = {
        'current_page': current_page,
        'service': service
        }
    return render(request, 'admin_app/pages/service_edit.html', context)

@login_required(login_url='/admin/login/')
def service_delete(request, service_id):
    try:
        service = Service.objects.get(id=service_id)
    except Service.DoesNotExist:
        messages.error(request, 'service not found')
        return redirect('service_list')
    
    try: 
        service.delete()
        messages.success(request, 'service deleted successfully')
        return redirect('service_list')
    except Exception as e:
        messages.error(request, f'Error deleting service: {e}')
        return redirect('service_list')


def profile(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'admin_app/pages/profile.html', context)

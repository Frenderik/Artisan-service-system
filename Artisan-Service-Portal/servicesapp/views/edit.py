# views.py

from django.shortcuts import get_object_or_404, render, redirect
from servicesapp.models import Service
from servicesapp.forms import ServiceForm  # Create a form for editing

def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
        return render(request, 'services/artisan/dashboard.html', {'services': Service.objects.all()})
  # Redirect to your services page after editing
    else:
        form = ServiceForm(instance=service)

    return render(request, 'services/artisan/edit_service.html', {'form': form, 'service': service})

# views.py

from django.shortcuts import get_object_or_404, render, redirect
from servicesapp.models import Service

def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    service.delete_service()
    return render(request, 'services/artisan/dashboard.html', {'services': Service.objects.all()})

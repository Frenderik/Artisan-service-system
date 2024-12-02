# views.py

from django.shortcuts import get_object_or_404, render
from servicesapp.models import Service

def toggle_service_filled(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    service.toggle_filled()
    return render(request, 'services/artisan/dashboard.html', {'services': Service.objects.all()})

# views.py
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView,DeleteView

from servicesapp.forms import ApplyServiceForm
from servicesapp.models import Service, Applicant

class AboutUsView(ListView):
    model = Service
    context_object_name = 'services'
    template_name = 'about_us.html'
    def get_queryset(self):
        return self.model.objects.all()[:6]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trendings'] = self.model.objects.filter(created_at__month=timezone.now().month)[:3]
        return context




    
    
    
 
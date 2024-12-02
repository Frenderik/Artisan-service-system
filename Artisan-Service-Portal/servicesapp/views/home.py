from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView,DeleteView

from servicesapp.forms import ApplyServiceForm
from servicesapp.models import Service, Applicant





class HomeView(ListView):
    model = Service
    template_name = 'home.html'
    context_object_name = 'services'
    
    def get_queryset(self):
        return self.model.objects.all()[:6]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trendings'] = self.model.objects.filter(created_at__month=timezone.now().month)[:3]
        return context


class SearchView(ListView):
    model = Service
    template_name = 'services/search.html'
    context_object_name = 'services'

    def get_queryset(self):
        return self.model.objects.filter(location__contains=self.request.GET['location'],
                                         title__contains=self.request.GET['service'])


class ServiceListView(ListView):
    model = Service
    template_name = 'services/services.html'
    context_object_name = 'services'
    paginate_by = 5


class ServiceDetailsView(DetailView):
    model = Service
    template_name = 'services/details.html'
    context_object_name = 'service'
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        obj = super(ServiceDetailsView, self).get_object(queryset=queryset)
        if obj is None:
            raise Http404("Service doesn't exists")
        return obj

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # redirect here
            raise Http404("Service doesn't exists")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class ApplyServiceView(CreateView):
    model = Applicant
    form_class = ApplyServiceForm
    slug_field = 'service_id'
    slug_url_kwarg = 'service_id'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.info(self.request, 'Successfully applied for the service!')
            return self.form_valid(form)
        else:
            return HttpResponseRedirect(reverse_lazy('service:home'))

    def get_success_url(self):
        return reverse_lazy('services:services-detail', kwargs={'id': self.kwargs['service_id']})

    # def get_form_kwargs(self):
    #     kwargs = super(ApplyServiceView, self).get_form_kwargs()
    #     print(kwargs)
    #     kwargs['service'] = 1
    #     return kwargs

    def form_valid(self, form):
        # check if user already applied
        applicant = Applicant.objects.filter(user_id=self.request.user.id, service_id=self.kwargs['service_id'])
        if applicant:
            messages.info(self.request, 'You already applied for this service')
            return HttpResponseRedirect(self.get_success_url())
        # save applicant
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView

from servicesapp.decorators import user_is_artisan
from servicesapp.forms import CreateServiceForm
from servicesapp.models import Service, Applicant


from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from accounts.forms import ArtisanProfileUpdateForm
from accounts.models import User



class DashboardView(ListView):
    model = Service
    template_name = 'services/artisan/dashboard.html'
    context_object_name = 'services'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_artisan)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(user_id=self.request.user.id)


class ApplicantPerServiceView(ListView):
    model = Applicant
    template_name = 'services/artisan/applicants.html'
    context_object_name = 'applicants'
    paginate_by = 1

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_artisan)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        return Applicant.objects.filter(service_id=self.kwargs['service_id']).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service'] = Service.objects.get(id=self.kwargs['service_id'])
        return context
    
# class ServiceCreateView(CreateView):
#     template_name = 'services/create.html'
#     form_class = CreateServiceForm
#     extra_context = {
#         'title': 'Post New Service'
        
#     }
#     success_url = reverse_lazy('services:artisan-dashboard')

#     @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
#     def dispatch(self, request, *args, **kwargs):
#         if not self.request.user.is_authenticated:
#             return reverse_lazy('accounts:login')
#         if self.request.user.is_authenticated and self.request.user.role != 'artisan':
#             return reverse_lazy('accounts:login')
#         return super().dispatch(self.request, *args, **kwargs)

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(ServiceCreateView, self).form_valid(form)
#         # return super().form_valid(form)


#     def post(self, request, *args, **kwargs):
        
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)


class ServiceCreateView(CreateView):
    template_name = 'services/create.html'
    form_class = CreateServiceForm
    extra_context = {
        'title': 'Post New Service'
    }
    success_url = reverse_lazy('services:artisan-dashboard')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('accounts:login')
        if self.request.user.is_authenticated and self.request.user.role != 'artisan':
            return reverse_lazy('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)





class ApplicantsListView(ListView):
    model = Applicant
    template_name = 'services/artisan/all-applicants.html'
    context_object_name = 'applicants'

    def get_queryset(self):
        # services = Service.objects.filter(user_id=self.request.user.id)
        return self.model.objects.filter(service__user_id=self.request.user.id)


@login_required(login_url=reverse_lazy('accounts:login'))
def filled(request, service_id=None):
    service = Service.objects.get(user_id=request.user.id, id=service_id)
    service.filled = True
    service.save()
    return HttpResponseRedirect(reverse_lazy('services:artisan-dashboard'))


class ArtisanEditProfileView(UpdateView):
    model = User
    form_class = ArtisanProfileUpdateForm
    context_object_name = 'artisan'
    template_name = 'services/artisan/edit-profile.html'
    success_url = reverse_lazy('accounts:artisan-profile-update')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_artisan)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("User doesn't exists")
        # context = self.get_context_data(object=self.object)
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        obj = self.request.user
        print(obj)
        if obj is None:
            raise Http404("service doesn't exists")
        return obj


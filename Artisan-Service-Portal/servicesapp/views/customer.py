from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from accounts.forms import CustomerProfileUpdateForm
from accounts.models import User
from servicesapp.decorators import user_is_customer


class CustomerEditProfileView(UpdateView):
    model = User
    form_class = CustomerProfileUpdateForm
    context_object_name = 'customer'
    template_name = 'services/customer/edit-profile.html'
    success_url = reverse_lazy('accounts:customer-profile-update')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_customer)
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

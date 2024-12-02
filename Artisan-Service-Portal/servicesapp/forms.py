from django import forms

from servicesapp.models import Service, Applicant, Contact


class CreateServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ('user', 'created_at',)

    def is_valid(self):
        valid = super(CreateServiceForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        service = super(CreateServiceForm, self).save(commit=False)
        if commit:
            service.save()
        return service


class ApplyServiceForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ('service',)

        
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number','message']


# forms.py

from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'type','category']  # Add all fields you want to edit



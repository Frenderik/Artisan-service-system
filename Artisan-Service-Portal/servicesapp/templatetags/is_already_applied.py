from django import template

from servicesapp.models import Applicant

register = template.Library()


@register.simple_tag(name='is_already_applied')
def is_already_applied(service, user):
    applied = Applicant.objects.filter(service=service, user=user)
    if applied:
        return True
    else:
        return False

from django.db import models
from django.utils import timezone

from accounts.models import User

SERVICE_TYPE = (
    ('1', "Contract"),
    ('2', "Piecework"),
    ('3', "Dailywork"),
)
SERVICE_CATEGORY=(

    ('1',"Masonry and concrete works"),
    ('2',"Furniture and Home Decors"),
    ('3',"Culinary Arts"),
    ('4',"Metalwork and Plumbing Services"),
    ('5',"Fine art and Painting artisans"),
    ('6',"Digital arts and Designs"),
    ('7',"Fashion Designs and Tailoring"),
    ('8',"Glass and Ceramics"),
    ('9',"Technology and Electronics"),
                               
    
)


class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    location = models.CharField(max_length=150)
    type = models.CharField(choices=SERVICE_TYPE, max_length=10)
    category = models.CharField(choices=SERVICE_CATEGORY, max_length=100)
    last_date = models.DateTimeField()
    company_name = models.CharField(max_length=100)
    company_description = models.CharField(max_length=300)
    website = models.CharField(max_length=100, default="", blank=True, null=True)    
    created_at = models.DateTimeField(default=timezone.now)
    filled = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title
    
    def toggle_filled(self):
        self.filled = not self.filled
        self.save()
    def delete_service(self):
        self.delete()


class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='applicants')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.get_full_name()
    #def __str__(self):
     #    return self.user.get_email()

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number= models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name

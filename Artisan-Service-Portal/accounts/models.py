from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError

from accounts.managers import UserManager

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'))


class User(AbstractUser):
    username = None
    profile_picture = models.ImageField(upload_to='media/img', default='DEFAULT VALUE')
    contact = models.CharField(max_length=10, blank=True, null=True)
    phone_number= models.CharField(max_length=10, blank=True, null=True)
    role = models.CharField(max_length=12, error_messages={
        'required': "Role must be provided"
    
    })
    gender = models.CharField(max_length=10, blank=True, null=True, default="")
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    def clean(self):
        # Add your custom validation logic here
        if "gmail.com" not in self.email:
            raise ValidationError("Email must be a valid Gmail address.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    objects = UserManager()

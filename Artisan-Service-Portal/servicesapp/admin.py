from django.contrib import admin

from servicesapp.models import Service,Applicant, Contact
from accounts.models import User
# Register your models here.


class  ServiceAdmin(admin.ModelAdmin):
  
  list_display=('title','created_at','last_date', 'filled')
  list_filter=('filled',)
  search_fields=('title',)

  def get_ordering(self, request):
     if request.user.is_superuser:
        return('title','created_at')
     return ('title',)
  
admin.site.register(Service, ServiceAdmin)



class UserAdmin(admin.ModelAdmin):
    list_display=('email','date_joined','gender','role','last_login')
    list_filter=('role',)
    search_fields=('role',)

    def get_ordering(self, request):
       if request.user.is_superuser:
          return('email','date_joined')
       return ('email',)
  
admin.site.register(User,UserAdmin)

class ContactAdmin(admin.ModelAdmin):
   list_display=('name','email','message', 'phone number')
   list_filter=('email',)
   search_fields=('email',)

   def get_ordering(self, request):
     if request.user.is_superuser:
        return('email')
     return ('email',)


admin.site.register(Contact)
class ApplicantAdmin(admin.ModelAdmin):
 
   list_display=('name','service','created_at')
   list_filter=('name',)
   search_fields=('service',)

   def get_ordering(self, request):
     if request.user.is_superuser:
        return('name')
     return ('name',)
   admin.site.register(Applicant)
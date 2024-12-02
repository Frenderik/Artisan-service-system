from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from servicesapp.views import CustomerEditProfileView,ArtisanEditProfileView
from .views import *

app_name = "accounts"

urlpatterns = [
    
    path('customer/register', RegisterCustomerView.as_view(), name='customer-register'),
    path('artisan/register', RegisterArtisanView.as_view(), name='artisan-register'),
    path('customer/profile/update', CustomerEditProfileView.as_view(), name='customer-profile-update'),
    path('artisan/profile/update', ArtisanEditProfileView.as_view(), name='artisan-profile-update'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('login', LoginView.as_view(), name='login'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include


admin.site.site_header='Artisan Portal admin'
admin.site.site_title='Artisan Portal admin'
admin.site.index_title='Artisan Portal administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('servicesapp.urls')),
    path('', include('accounts.urls')),
]

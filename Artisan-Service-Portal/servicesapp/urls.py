from django.urls import path, include

from .views import *



app_name = "services"

urlpatterns = [

        path('edit-service/<int:service_id>/', edit_service, name='edit-service'),

        path('delete-service/<int:service_id>/', delete_service, name='delete-service'),

    path('toggle-filled/<int:service_id>/', toggle_service_filled, name='toggle-service-filled'),


    path('initiate-paypal-checkout/', initiate_paypal_checkout, name='initiate_paypal_checkout'),

    path('contact/', contact_us, name='contact_us'),
   
    path('about-us/', AboutUsView.as_view(), name='about_us'),
    path('', HomeView.as_view(), name='home'),
    path('search', SearchView.as_view(), name='searh'),
    path('artisan/dashboard', include([
        path('', DashboardView.as_view(), name='artisan-dashboard'),
        path('all-applicants', ApplicantsListView.as_view(), name='artisan-all-applicants'),
        path('applicants/<int:service_id>', ApplicantPerServiceView.as_view(), name='artisan-dashboard-applicants'),
        path('mark-filled/<int:service_id>', filled, name='service-mark-filled'),
    ])),
    path('apply-service/<int:service_id>', ApplyServiceView.as_view(), name='apply-service'),
    path('services', ServiceListView.as_view(), name='services'),
    path('services/<int:id>', ServiceDetailsView.as_view(), name='services-detail'),
    path('artisan/services/create', ServiceCreateView.as_view(), name='artisan-services-create'),
    #path('edit-service/<int:pk>/', EditServiceView.as_view(), name='edit_service'),
    path('initiate-paypal-checkout/', initiate_paypal_checkout, name='initiate_paypal_checkout'),
    path('capture-paypal-payment/', capture_paypal_payment, name='capture_paypal_payment'),
    # Add other URLs as needed  
]


from django.shortcuts import render

def initiate_paypal_checkout(request):
    return render(request, 'initiate_paypal_checkout.html')
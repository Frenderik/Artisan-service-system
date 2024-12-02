# views.py

from django.http import JsonResponse
from paypalrestsdk import Payment

def capture_paypal_payment(request):
    payment_id = request.GET.get('paymentId')
    payment = Payment.find(payment_id)
    
    if payment.execute({"payer_id": request.GET.get('PayerID')}):
        # Payment was successful, handle accordingly (e.g., update database)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': payment.error})

# views.py
from django.shortcuts import render, redirect
from servicesapp.forms import ContactForm

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Assuming you have a success page
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

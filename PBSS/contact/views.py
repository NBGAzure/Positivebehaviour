from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

def contact(request):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            messages.success(request, 'Your request for contact has been updated')
            form.save()

        context ={
            'form': form
        }
        return render(request, 'contact.html', context)

from django.shortcuts import render, redirect
from django.contrib import messages
from positivebehaviour.models import NewsletterUsers
from positivebehaviour.forms import NewsletterUserSignUpform


def freefbaform(request):
    return render(request, "freefbaform/freefbaform.html")


def newsletter_signup(request):
    form = NewsletterUserSignUpform(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUsers.objects.filter(email=instance.email).exists():
            messages.success(request, f'Sorry this email already exist')
            return redirect('index')
        else:
            instance.save()
            messages.success(request, f'Email is saved successfully')
    context = {
        'form': form,
    }
    template = "positivebehaviour/base.html"
    return render(request, template, context)

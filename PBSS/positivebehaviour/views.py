from django.core.checks import messages
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import render

from .models import NewsletterUsers
from .forms import NewsletterUserSignUpform


# Create your views here.
def index(request):
    form = NewsletterUserSignUpform(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUsers.objects.filter(email=instance.email).exists():
            messages.success(request, f'This email already exist')
            return redirect('index')
        else:
            instance.save()
            messages.success(request, f'Your request for subscription has been updated')
            return redirect('index')
    context = {
        'form': form,
    }
    template = "positivebehaviour/base.html"
    #  return render(request, template, context)
    return render(request, 'positivebehaviour/index.html', context)


def sitemap(request):
    return render(request, 'positivebehaviour/sitemap.html', {'title': 'sitemap'})


def fbaForm(request):
    return render(request, 'fbaform/fbaform.html', {'title': 'fbaform'})


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


def newsletter_unsubcribe(request):
    form = NewsletterUserSignUpform(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUsers.objects.filter(email=instance.email).exists():
            NewsletterUsers.objects.filter(email=instance.email).delete()
        else:
            print("sorry we couldnt find your email address")

    context = {
        "form": form,
    }
    template = "positivebehaviour/base.html"
    return render(request, template, context)

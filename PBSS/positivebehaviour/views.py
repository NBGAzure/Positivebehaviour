from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    form = NewsletterUserSignUpform(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUsers.objects.filter(email=instance.email).exists():
            print("Sorry this email already exist")
        else:
            instance.save()
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



from django.shortcuts import render

from .models import NewsletterUsers
from .forms import NewsletterUserSignUpform

def newsletter_signup(request):
    form = NewsletterUserSignUpform(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUsers.objects.filter(email=instance.email).exists():
            print("Sorry this email already exist")
        else:
            instance.save()

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
        "form":form,
    }
    template = "positivebehaviour/base.html"
    return render(request, template, context)





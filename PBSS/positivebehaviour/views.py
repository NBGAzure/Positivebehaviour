from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):

    return render(request, 'positivebehaviour/index.html', {'title': 'home'})

def sitemap(request):

    return render(request, 'positivebehaviour/sitemap.html', {'title': 'sitemap'})

def fbaForm(request):

    return render(request, 'fbaform/fbaform.html', {'title': 'fbaform'})





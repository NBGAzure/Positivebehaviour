from django.shortcuts import render
from django.http import HttpResponse
from .models import Fba_Antecedent

# Create your views here.




def index(request):

    antecedent = Fba_Antecedent.objects.all()[:10]

    context = {

        'title' : 'Antecedents',
        'posts' : antecedent
    }


    #return HttpResponse('FBA FORM')
    return render(request, 'posts/index.html', context)

def details(request, id):
    post = Fba_Antecedent.objects.get(id=id)

    context = {
        'post': post
    }

    return render(request, 'posts/details.html', context)
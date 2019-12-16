from django.shortcuts import render
from django.http import HttpResponse


from django.shortcuts import render, redirect
from .models import List
from .models import Anticident
from .forms import ListForm
from .forms import AnticidentForm
from django.contrib import messages
from .forms import Fba
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def fbaform(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Behaviour has been added to the list'))
            return render(request, 'fbaform/fbaform.html', {'all_items': all_items})
    else:
        all_items = List.objects.all
        return render(request, 'fbaform/fbaform.html', {'all_items': all_items})


def anticident(request):
    if request.method == 'POST':
        form = AnticidentForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_anticident = Anticident.objects.all
            messages.success(request, ('Anticident has been added to the list'))
            return render(request, 'fbaform/fbaform.html', {'all_anticident': all_anticident})
    else:
        all_anticident = Anticident.objects.all
        return render(request, 'fbaform/fbaform.html', {'all_anticident': all_anticident})

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Behaviour has been deleted'))
    return redirect('fbaform')

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('fbaform')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('fbaform')

def edit(request, list_id):
    if request.method == "POST":
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, ('Edited'))
            return redirect('fbaform')
    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'fbaform/editfbaform.html', {'item': item})



def get(self, request):
    form = Fba()
    return render(request,{'form':form} )

def post (self, request):
    form = Fba(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        text = form.cleaned_data['post']
        form = Fba()

    args = {'form': form, 'text': text}
    return render(request, args)

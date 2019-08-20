from django.shortcuts import render
from .forms import FbaForm

def home(request):
    return render(request, 'form/home.html')

def order(request):
    if request.method == 'POST':
        filled_form = FbaForm(request.POST)
        if filled_form.is_valid():
            note = 'Thanks for ordering! Your %s %s and %s pizza is on its way!' %(filled_form.cleaned_data['size'], filled_form.cleaned_data['behaviour1'], filled_form.cleaned_data['behaviour2'],)
        else:
            note = 'Order was not created, please try again'
        new_form = FbaForm()
        return render(request, 'form/order.html', {'FbaForm':new_form, 'note':note})
    else:
        form = FbaForm()
        return render(request, 'form/order.html', {'FbaForm':form})
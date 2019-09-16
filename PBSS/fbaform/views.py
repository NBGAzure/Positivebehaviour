from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Location


def fbaformfunc(request):
    location_all = Location.objects.all()
    return render(request, 'fbaform/fbaform.html',
        {'all_items': location_all})
#
# def addLocaion(request):
#     all_location = Location.objects.all()
#     return render(request,'firstapp.html', {'locationall': all_location})
#
def addBehaviour(request):
    new_entry = Location(wakingup=request.POST['wakingup'])
    new_entry.save()
    return HttpResponseRedirect('/fbaform/')
# def deletePbss(request, Datetime_id):
#     to_delete = fbaformfunc.objects.get(id=Datetime_id)
#     to_delete.delete()
#     return HttpResponseRedirect('/first_app/')
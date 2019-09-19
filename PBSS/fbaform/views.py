from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Location, Triggers


def fbaformfunc(request):
    location_all = Location.objects.all()
    return render(request, 'fbaform/fbaform.html',
        {'all_items': location_all})

def addBehaviour(request):
    new_entry = Location(wakingup=request.POST['wakingup'])
    new_entry.save()
    return HttpResponseRedirect('/fbaform/')

# def deletePbss(request, Datetime_id):
#     to_delete = fbaformfunc.objects.get(id=Datetime_id)
#     to_delete.delete()
#     return HttpResponseRedirect('/first_app/')

def triggers(request):
    triggers_all = Triggers.objects.all()
    return render(request, 'fbaform/fbaform.html',
                  {'all_trigger': triggers_all})
def addTrigger (request):
    new_entry_trig = Triggers(reason1=request.POST['reason1'])
    new_entry_trig.save()
    return HttpResponseRedirect('/fbaform/')


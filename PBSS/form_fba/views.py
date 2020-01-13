from django.shortcuts import render, redirect
from form_fba.forms import FbaForm, EditFba
from form_fba.models import Fba, User
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.models import User
# from .forms import EditFba


from .forms import forms
from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse, HttpResponseRedirect

# Create your views here.


def std(request):
    if request.method == 'POST':
        form = FbaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                pass
    else:
        form = FbaForm()
    return render(request, 'fbaindex.html', {'form': form})



#
# def view(request):
#     form_fba = Fba.objects.all()
#     return render(request, "view.html", {'form_fba': form_fba})

class fbaChart(TemplateView):
    template_name = 'charts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Fba.objects.all()
        return context

def brreport(request):

    return render(request, 'brreport.html', {'title': 'Br Report'})


def delete(request, id):
    form_fba = Fba.objects.get(id=id)
    form_fba.delete()
    messages.success(request, ' The following user is now deleted!')
    return redirect("/view")

# def edit(request, id=None):
#     instance = Fba.objects.get(id=id)
#     form = EditFba(request.POST or None, instance=instance)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#         return HttpResponseRedirect(instance.get_absolute_url())
#
#     context={'form': form}
#     return render(request, "edit.html", context)



# def std(request):
#     if request.method == "POST":
#         form = FbaForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('/view')
#             except:
#                 pass
#     else:
#         form = FbaForm()
#     return render(request, 'fbaindex.html', {'form': form})

# def edit(request,id=None):
#     instance = get_object_or_404(Fba, id=id)
#     form_fba = EditFba(request.POST or None, instance=instance)
#     if form_fba.is_valid():
#         instance = form_fba.save(commit=False)
#         instance.save()
#         return HttpResponseRedirect(instance.get_absolute_url())
#
#     context = {
#         "instance": instance,
#     }
#     return render(request, "edit.html", context)


def edit(request, id):
    instance = Fba.objects.get(id=id)

    if request.method == 'POST':

        user_form = EditFba(request.POST, instance=instance)
        if user_form.is_valid():

            instance = user_form.save(commit=False)
            instance.save()

            return redirect('/view')

    context = {
                "form_fba": instance,
            }
    messages.success(request, ' The following user information is now updated!')
    return render(request, "edit.html", context)



#
# def edit(request, id):
#     instance = Fba.objects.get(id=id)
#     if request.method == "POST":
#         form = EditFba(request.POST, instance = instance)
#         if form.is_valid():
#             messages.success(request, ' in the loop!')
#             instance = form.save(commit=False)
#             instance.save()
#             messages.success(request, ' end loop')
#             return redirect('view.html')
#     else:
#         form = EditFba(instance=instance)
#     template_name = 'fbaindex.html'
#
#     context = {
#                 "form_fba": form,
#             }
#
#     return render(request, template_name, context)

def view(request):
    #instance = Fba.objects.get(id=id)
    instance = Fba.objects.all()
    #instance = Fba.objects.get(id=id)

    if instance in request.user.fba.all():
        template = 'view.html'
        context = {
            'form_fba': instance,
                }
        return render(request, template, context)
    return render(request, "view.html")

# def view(request):
#     form_fba = Fba.objects.all()
#     return render(request, "view.html", {'form_fba': form_fba})

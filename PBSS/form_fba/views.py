from django.shortcuts import render, redirect
from form_fba.forms import FbaForm
from form_fba.models import Fba
from django.contrib import messages
from django.views.generic import TemplateView
from .forms import EditFba


from .forms import forms
from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse, HttpResponseRedirect

# Create your views here.


def std(request):
    if request.method == "POST":
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




def view(request):
    form_fba = Fba.objects.all()
    return render(request, "view.html", {'form_fba': form_fba})

class fbaChart(TemplateView):
    template_name = 'charts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Fba.objects.all()
        return context

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
        user_form = EditFba(request.POST, instance = instance )
        if user_form.is_valid():
            messages.success(request, ' in the loop!')
            instance = user_form.save(commit=False)
            instance.save()
            messages.success(request, ' end loop')
            return self.cleaned_data

    context = {
                "form_fba": instance,
            }

    return render(request, "edit.html", context)

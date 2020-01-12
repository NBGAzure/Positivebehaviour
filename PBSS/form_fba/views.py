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

def brreport(request):

    return render(request, 'brreport.html', {'title': 'Br Report'})


def delete(request, id):
    form_fba = Fba.objects.get(id=id)
    form_fba.delete()
    messages.success(request, ' The following user is now deleted!')
    return redirect("/view")



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






# def edit(request, id=None):
#     u1 = get_object_or_404(Fba, id=id)
#     user_form = Fba(request.POST, instance=u1)
#     if user_form.is_valid():
#             form_fba = user_form.save(commit=False)
#             form_fba.save()
#             return HttpResponseRedirect(form_fba.get_absolute_url())
#
#     # if request.method == "POST":
#     #     form = FbaForm(request.POST)
#     #     if form.is_valid():
#     #
#
#     messages.success(request, ' The following user information is now updated!')
#     # context = {
#     #     'form_fba': form_fba,
#     #     'user_form': user_form,
#     # }
#     return render(request, "view.html", {"u1": u1})








#
#
# def edit(request, id=None):
#     user = get_object_or_404(Fba, id=id)
#     user_form = EditFba(request.POST or None, user=user)
#     if user_form.is_valid():
#         user = EditFba.save(commit=False)
#         user.save()
#         return HttpResponseRedirect(user.get_absolute_url())
#
#     context = {
#
#         "user": user,
#
#     }
#     return render(request, "edit.html", context)
#

#
def edit(request, id):
    form_fba = Fba.objects.get(id=id)
    if request.method == 'POST':
        user_form = Fba(request.POST, instance=request.Fba)
        if user_form.is_valid():
            user_form.save()
    context = {
                "form_fba": form_fba,
            }
    messages.success(request, ' The following user information is now updated!')
    return render(request, "edit.html", context)


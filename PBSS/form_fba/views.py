from django.shortcuts import render, redirect
from form_fba.forms import FbaForm, EditFba, brForm
from form_fba.models import Fba, User, Br
from django.contrib import messages
from django.views.generic import TemplateView,ListView
from django.db.models import Sum
from django.db.models import Avg, Count
from django.db.models import Sum
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
                messages.warning(request, 'Please keep limit between 0 and 10!')
                pass
    else:
        form = FbaForm()
    return render(request, 'fbaindex.html', {'form': form})

def view(request):
    form_fba = Fba.objects.all()
    return render(request, "view.html", {'form_fba': form_fba})

def std1(request):
    if request.method == 'POST':
        form = brForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view1')
            except:
                pass
    else:
        form = brForm()
    return render(request, 'brreport.html', {'form': form})

def view1(request):
    form_br = Br.objects.all()
    # sum = (Br.objects.aggregate(
    #     total=Sum('sum', field="intensity1+intensity2+intensity3+intensity4+intensity5")
    # )['sum']
    # )
    # sum = sum.aggregate(sum=Sum('item_quantity'))['sum'] or 0
    # context = {
    #     'sum': sum,
    # }
    return render(request, "brview.html", {'form_br': form_br})

def view1(request):
    instance = Br.objects.all()

    template = 'brview.html'
    context = {
        'form_br': instance,
    }
    return render(request, template, context)

class fbaChart(TemplateView):
    template_name = 'charts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Br.objects.all()
        return context


# def brreport(request):
#     return render(request, 'brreport.html', {'title': 'Br Report'})


def delete(request, id):
    form_fba = Fba.objects.get(id=id)
    form_fba.delete()
    messages.success(request, ' The following user is now deleted!')
    return redirect("/view")




def edit(request, id):
    instance = Fba.objects.get(id=id)

    if request.method == 'POST':

        user_form = EditFba(request.POST, instance = instance )
        if user_form.is_valid():

            instance = user_form.save(commit=False)
            instance.save()
            messages.success(request, ' The client information is now updated!')
            return redirect('/view')
        else:
            messages.warning(request, 'Please keep limit between 0 and 10!')
    context = {
                "form_fba": instance,
            }

    return render(request, "edit.html", context)


def view(request):

    instance = Fba.objects.all()
    # instance = Fba.objects.filter(client_id=33)

    template = 'view.html'
    context = {
        'form_fba': instance,
    }
    return render(request, template, context)

class fbaListView(ListView):
    model = Fba
    template_name = 'view.html'
    context_object_name = 'form_fba'
    ordering = ['-date_created']













    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)
    #
    # def get_queryset(self):
    #     return super(view, self).get_queryset().filter(author=self.request.user)


###TESTING IN PROGRESS






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




#TESTING - FOUND differences >> current
# def edit(request, id):
#     instance = Fba.objects.get(id=id)
#
#     if request.method == 'POST':
#
#         user_form = EditFba(request.POST, instance=instance)
#         if user_form.is_valid():
#             instance = user_form.save(commit=False)
#             instance.save()
#
#             return redirect('/view')
#
#     context = {
#         "form_fba": form_fba,
#     }
#     messages.success(request, ' The following user information is now updated!')
#     return render(request, "edit.html", context)
#

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



##Testing in PROGRESS..DO NOT REMOVE>>cu


# def view(request):
#     form_fba = Fba.objects.all()
#     return render(request, "view.html", {'form_fba': form_fba})


##TESTING IN PROGRESS >>Current

# def view(request):
#     form_fba = Fba.objects.all()
#     return render(request, "view.html", {'form_fba': form_fba})
#
#     context["qs"] = Fba.objects.all()
#     return context

from typing import Type
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Post
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account is now created for {username}!')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account is now updated!')
            return redirect('client')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    form = UserCreationForm
    return render(request=request,
                  template_name="users/profile.html",
                  context={"form": form})
   # return render(request, 'users/profile.html', context, {'title': 'Profile'})


def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account is now updated!')
            return redirect('client')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, "users/edit_profile.html", context, {'title': 'Profile'})


def client(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'users/profile.html', context)


class PostListView(LoginRequiredMixin,  ListView):
    model = Post
    template_name = 'users/profile.html'
    context_object_name = 'posts'
    ordering = ['-date_issued']
    paginate_by = 4

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return super(PostListView, self).get_queryset().filter(author=self.request.user)


class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'users/profile.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_issued')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    email = forms.EmailField(required='true', label=(''), max_length=30,
                             widget=forms.TextInput(attrs={"placeholder": "Email"}))
    client_name = forms.CharField(label=(''), max_length=30,
                               widget=forms.TextInput(attrs={"placeholder": "Username"}))
    content = forms.CharField(required='true', label=(''), max_length=30,
                             widget=forms.TextInput(attrs={"placeholder": "Content"}))
    model = Post
    fields = ['client_name', 'DOB', 'email', 'location', 'history', 'gender', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['client_name', 'DOB', 'email', 'location', 'history', 'gender', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/client'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
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
                "form_fba": form_fba,
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

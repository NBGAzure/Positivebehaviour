from typing import Type
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from users.models import Post
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render


def blregister(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account is now created for a support worker {username}!')
            return redirect('supportworker')
    else:
        form = UserRegisterForm()
    return render(request, 'businessleader/base.html', {'form': form})


class PostListViewBl(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'businessleader/userlist.html'
    context_object_name = 'posts'
    ordering = ['-date_issued']
    paginate_by = 4


class PostDetailViewBl(DetailView):
    model = User
    template_name = 'businessleader/user_detail.html'


def PostListViewBlSw(request):

    context = {
        'users': User.objects.all()
    }


    return render(request, 'businessleader/swlist.html', context)


# delete functionality of support worker in progress

class PostDeleteViewBl(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    success_url = '/businessleader'
    success_message = 'Support worker deleted successfully!'
    # template_name = 'businessleader/user_confirm_delete.html'


    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(PostDeleteViewBl, self).delete(request, *args, **kwargs)


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
           return True
        return False

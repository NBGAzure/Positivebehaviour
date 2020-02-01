from django.shortcuts import render
from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm


def client(request):
    form = UserCreationForm
    return render(request=request,
                  template_name="users/profile.html",
                  context={"form": form})

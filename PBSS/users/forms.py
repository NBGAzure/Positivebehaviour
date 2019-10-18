from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.forms.widgets import PasswordInput


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required='true', label=(''), max_length=30,
                                 widget=forms.TextInput(attrs={"placeholder": "Email"}))
    username = forms.CharField(label=(''), max_length=30,
                                 widget=forms.TextInput(attrs={"placeholder": "Username"}))
    password1 = forms.CharField(label=(''), widget=PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label=(''), widget=PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label=(''), max_length=30,
                             widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(label=(''), max_length=30,
                               widget=forms.TextInput(attrs={"placeholder": "Username"}))

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

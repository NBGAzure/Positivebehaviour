from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    email = forms.EmailField(required='true', label=(''), max_length=30,
                             widget=forms.TextInput(attrs={"placeholder": "Email"}))
    first_name = forms.CharField(label=(''), max_length=30,
                                 widget=forms.TextInput(attrs={"placeholder": "First name"}))
    last_name = forms.CharField(label=(''), max_length=30,
                                widget=forms.TextInput(attrs={"placeholder": "last name"}))
    message = forms.CharField(label=(''), max_length=300,
                              widget=forms.TextInput(attrs={"placeholder": "Message"}))

    class Meta:
        model = Contact
        fields = {'first_name', 'last_name', 'email', 'message'}

from django import forms
from .models import List
from .models import Anticident

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed"]

class AnticidentForm(forms.ModelForm):
    class Meta:
        model = Anticident
        fields = ["anticident", "completed"]


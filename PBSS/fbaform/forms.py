from django import forms
from .models import List
from .models import Anticident
from .models import Anti
from .models import Beh
from .models import Con


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed"]


class AnticidentForm(forms.ModelForm):
    class Meta:
        model = Anticident
        fields = ["anticident", "completed"]


class Fba(forms.ModelForm):
    post = forms.CharField()

    class Meta:
        model = Anti
        fields = ('post',)

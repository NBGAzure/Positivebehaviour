from django import forms
from .models import Fba


class FbaForm(forms.ModelForm):
    class Meta:
        model = Fba
        fields = "__all__"

class EditFba(forms.ModelForm):
    class Meta:
        model = Fba
        fields = [
            'user',
            'anticedent',
            'behaviour',
            'consequence',
            'intensity',
        ]
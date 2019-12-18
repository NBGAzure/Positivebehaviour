from django import forms
from form_fba.models import Fba


class FbaForm(forms.ModelForm):
    class Meta:
        model = Fba
        fields = "__all__"

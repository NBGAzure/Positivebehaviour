from django import forms
from .models import Fba



class FbaForm(forms.ModelForm):
    class Meta:
        model = Fba
        fields = (
        'user',
        'anticedent',
        'behaviour',
        'consequence',
        'intensity'
        )

    def save(self, commit=True):
        user = super(FbaForm, self).save(commit=False)
        user.anticedent = self.cleaned_data['anticedent']
        user.behaviour = self.cleaned_data['behaviour']
        user.consequence = self.cleaned_data['consequence']
        user.intensity = self.cleaned_data['intensity']
        if commit:
            user.save()
        return user

class EditFba(forms.ModelForm):
    class Meta:
        model = Fba
        fields = (

        'anticedent',
        'behaviour',
        'consequence',
        'intensity'
        )

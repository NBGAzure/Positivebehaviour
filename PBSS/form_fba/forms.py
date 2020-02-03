from django import forms
from .models import Fba, Br
from .models import User
from users.models import Post


class FbaForm(forms.ModelForm):
    class Meta:
        model = Fba
        fields = (
            'client',
            'anticedent',
            'behaviour',
            'consequence',
            'intensity'
        )

    def save(self, commit=True):
        #client = super(Post, self).save(commit=False)
        client = super(FbaForm, self).save(commit=False)
        client.anticedent = self.cleaned_data['anticedent']
        client.behaviour = self.cleaned_data['behaviour']
        client.consequence = self.cleaned_data['consequence']
        client.intensity = self.cleaned_data['intensity']
        if commit:
            client.save()
        return client


class EditFba(forms.ModelForm):
    class Meta:
        model = Fba
        fields = (
            'anticedent',
            'behaviour',
            'consequence',
            'intensity'
        )

class brForm(forms.ModelForm):
    class Meta:
        model = Br
        fields = (
        'client',
        'intensity1',
        'intensity2',
        'intensity3',
        'intensity4',
        'intensity5',
        )

    def save(self, commit=True):
        client = super(Post, self).save(commit=False)
        client.intensity1 = self.cleaned_data['intensity1']
        client.intensity2 = self.cleaned_data['intensity2']
        client.intensity3 = self.cleaned_data['intensity3']
        client.intensity4 = self.cleaned_data['intensity4']
        client.intensity5 = self.cleaned_data['intensity5']
        if commit:
            client.save()
        return client

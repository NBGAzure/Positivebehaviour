from django import forms
from .models import Fba
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
        client = super(Post, self).save(commit=False)
        client.anticedent = self.cleaned_data['anticedent']
        client.behaviour = self.cleaned_data['behaviour']
        client.consequence = self.cleaned_data['consequence']
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

# class brForm(forms.ModelForm):
#     class Meta:
#         model = Br
#         fields = (
#         'client',
#         )
#
#     def save(self, commit=True):
#         client = super(Post, self).save(commit=False)
#         if commit:
#             client.save()
#         return client
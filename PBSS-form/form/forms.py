from django import forms

class FbaForm(forms.Form):
    behaviour1 = forms.CharField(label='Behaviour 1', max_length=100)
    behaviour2 = forms.CharField(label='behaviour2', max_length=100)
    intensity = forms.ChoiceField(label='intensity', choices=[('*','*'),('**','**'),('***','***'),('****','****'),('*****','*****')])


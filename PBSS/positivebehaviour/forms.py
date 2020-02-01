from django import forms

from .models import NewsletterUsers


class NewsletterUserSignUpform(forms.ModelForm):
    class Meta:
        model = NewsletterUsers
        fields = {'email'}

        def clean_email(self):
            email = self.cleaned_data.get('email')

            return email

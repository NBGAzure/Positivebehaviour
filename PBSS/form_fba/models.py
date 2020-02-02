from django.forms import ModelForm, Textarea
from django.db import models
from users.models import Post, User
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
# Create your models here.

class Fba(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    anticedent = models.CharField(blank=False, max_length=200)
    behaviour = models.CharField(blank=False, max_length=200)
    consequence = models.CharField(blank=False, max_length=200)
    intensity = models.PositiveSmallIntegerField(blank=False, validators=[MinValueValidator(0), MaxValueValidator(10)])
    client_fk = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, default=None)

    def get_absolute_url(self):
        return reverse("forms:detail", kwargs={"is": self.id})


class Meta:
    db_table = 'fba'

#
# class Br(models.Model):
#     client = models.ForeignKey(Post, on_delete=models.CASCADE)
#
#     def get_absolute_url(self):
#         return reverse("forms:detail", kwargs={"is": self.id})
#
#
# class Meta:
#     db_table = 'fba'

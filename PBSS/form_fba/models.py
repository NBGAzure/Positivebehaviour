from django.forms import ModelForm, Textarea
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Fba(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anticedent = models.CharField(max_length=200)
    behaviour = models.CharField(max_length=200)
    consequence = models.CharField(max_length=200)
    intensity = models.IntegerField()

class Meta:
    db_table = 'fba'
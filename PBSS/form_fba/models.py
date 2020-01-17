from django.forms import ModelForm, Textarea
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Fba(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="fba", null=True)
    anticedent = models.CharField(blank=False, max_length=200)
    behaviour = models.CharField(blank=False, max_length=200)
    consequence = models.CharField(blank=False, max_length=200)
    intensity = models.PositiveSmallIntegerField(blank=False, validators=[MinValueValidator(0), MaxValueValidator(10)])

    def get_absolute_url(self):
        return reverse("forms:detail", kwargs={"is": self.id})


class Meta:
    db_table = 'fba'



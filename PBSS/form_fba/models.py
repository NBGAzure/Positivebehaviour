from django.forms import ModelForm, Textarea
from django.db import models
from users.models import Post
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Fba(models.Model):
    client = models.ForeignKey(Post, on_delete=models.CASCADE)
    anticedent = models.CharField(blank=False, max_length=200)
    behaviour = models.CharField(blank=False, max_length=200)
    consequence = models.CharField(blank=False, max_length=200)
    intensity = models.PositiveSmallIntegerField(blank=False, validators=[MinValueValidator(0), MaxValueValidator(10)])

    def get_absolute_url(self):
        return reverse("forms:detail", kwargs={"is": self.id})


class Meta:
    db_table = 'fba'



from django.db import models
from datetime import datetime

# Create your models here.
class Fba_Antecedent(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

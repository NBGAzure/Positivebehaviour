from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


class Post(models.Model):
    client_name = models.CharField(max_length=100)
    DOB = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    email = models.EmailField()
    content = models.TextField()
    date_issued = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        return reverse('client')

    "Below lines were to resize the profile pic images, however, It won't work with AWS"
    "def save(self):"
    "super().save()"

    "img = Image.open(self.image.path)"

    "if img.height > 300 or img.width > 300:"
    "output_size = (300, 300)" \
    "img.thumbnail(output_size)"
    "img.save(self.image.path)"

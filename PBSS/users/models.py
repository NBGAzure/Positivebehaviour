from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
<<<<<<< HEAD
=======
from datetime import datetime, date
>>>>>>> f0b6e1e02998a9fb873eb5e1342154cd2d91a7de
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


class Post(models.Model):
    client_name = models.CharField(max_length=100)
<<<<<<< HEAD
=======
    DOB = models.DateField(auto_now_add=False, auto_now=False, blank=True)
>>>>>>> f0b6e1e02998a9fb873eb5e1342154cd2d91a7de
    email = models.EmailField()
    content = models.TextField()
    date_issued = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

<<<<<<< HEAD
=======

>>>>>>> f0b6e1e02998a9fb873eb5e1342154cd2d91a7de
    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
<<<<<<< HEAD
        return reverse('client-detail', kwargs={'pk': self.pk})
=======
        return reverse('client')
>>>>>>> f0b6e1e02998a9fb873eb5e1342154cd2d91a7de

    "Below lines were to resize the profile pic images, however, It won't work with AWS"
    "def save(self):"
    "super().save()"

    "img = Image.open(self.image.path)"

    "if img.height > 300 or img.width > 300:"
    "output_size = (300, 300)" \
    "img.thumbnail(output_size)"
    "img.save(self.image.path)"

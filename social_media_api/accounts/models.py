from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom user model
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_photos/', default='profile_photos/default_photo.png', blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')

    def __str__(self):
        return self.username
    
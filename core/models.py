from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    age = models.IntegerField(default=0)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.DO_NOTHING)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:20]


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,  related_name='profile', on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.user.username} profile'


class Vote(models.Model):
    comment = models.ForeignKey(
        Comment, related_name='votes', on_delete=models.CASCADE)
    voted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

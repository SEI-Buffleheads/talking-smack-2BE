from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class User_profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, default=None)
    avatar = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User_profile, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Post by {self.content}'


class Comment(models.Model):
    user = models.ForeignKey(
        User_profile, on_delete=models.CASCADE, default=None)
    content = models.CharField(max_length=255, default=None)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user}'

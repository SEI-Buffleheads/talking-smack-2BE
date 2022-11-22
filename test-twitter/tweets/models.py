from django.db import models
# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    avatar = models.CharField(max_length=500)
    password = models.CharField(max_length=128)
    creation_date = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.username

class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.title} by {self.author}'
    

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='comments', default=None)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment {self.body} by {self.author}'
from turtle import title
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()
    		
    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    slug = models.SlugField()
    thumbnail = models.ImageField()
    
    def __str__(self):
        return self.title
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    overview = models.CharField(max_length=255)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=10000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category) 
    featured = models.BooleanField()
    
    def __str__(self):
        return self.title
    

    


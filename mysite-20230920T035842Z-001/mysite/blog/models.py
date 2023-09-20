from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django_extensions.db.fields import AutoSlugField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    body = RichTextField()
    slug = models.SlugField(null=True, unique = True, blank = True)

    authenticated = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.title + " by " + str(self.author)

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'slug': self.slug})



class Resource(models.Model):
    title = models.CharField(max_length = 255)
    

    created_on = models.DateTimeField(auto_now_add=True)
    body = RichTextField()
    slug = models.SlugField(null=True, unique = True, blank = True)

   
    
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.title 
    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'slug': self.slug})
class Engage(models.Model):
    title = models.CharField(max_length = 255)
    

    created_on = models.DateTimeField(auto_now_add=True)
    body = RichTextField()
    slug = models.SlugField(null=True, unique = True, blank = True)

   
    
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.title 
    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'slug': self.slug})

   

from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse, redirect

# Create your models here.
User = get_user_model()

class Note(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notes:detail', kwargs={'slug':self.slug})

    

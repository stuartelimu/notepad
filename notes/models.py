from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse, redirect

# Create your models here.
User = get_user_model()

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notes:detail', kwargs={'pk':self.pk})

    

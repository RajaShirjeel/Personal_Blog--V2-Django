from typing import Iterable
from django.db import models
from django.utils.text import slugify

from users.models import CustomUser

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='posts/images/')
    heading = models.CharField(max_length=200, blank=False)
    text = models.TextField(blank=False)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return f"Created by {self.creator} on {self.created_on}"
    
    def save(self, *args, **kwargs) -> None:
        if not self.slug: 
            self.slug = slugify(self.heading)
        super().save(*args, **kwargs)
    
    class Meta: 
        ordering = ['-created_on']

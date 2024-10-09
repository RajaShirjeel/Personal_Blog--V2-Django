from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length = 100, unique = True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    slug = models.SlugField(unique = True, blank = True)
    USERNAME_FIELD = 'email' # uses email as the default for login 
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.username} - {self.email}'
    
    def save(self, *args, **kwargs):
        if not self.slug: 
            base_slug = slugify(self.username)
            self.slug = base_slug
        super().save(*args, **kwargs)

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = get_user_model()
    published_date = models.DateTimeField(auto_now_add=True)
from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from login.models import *


class News(models.Model):
    title = models.CharField(max_length=150)
    description = RichTextField()
    thumbnails = models.ImageField(upload_to='thumbnails')
    date = models.DateField(auto_now=True)
    category = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)
    globalnews = models.BooleanField(default=False)
    latestnews = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='title',
                         unique=True, blank=True, null=True, default=None)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class FlashNews(models.Model):
    flash_news = models.CharField(max_length=500, null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.flash_news

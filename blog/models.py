from enum import _auto_null
from unittest.util import _MAX_LENGTH

from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length = 100)
    subtitle = models.CharField(max_length = 100)
    content = RichTextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="blog/%Y/%m/%d/")
    facebook = models.URLField(max_length=100, blank=True)
    twitter = models.URLField(max_length=100, blank=True)
    linkedin = models.URLField(max_length=100, blank=True)
    youtube = models.URLField(max_length=100, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
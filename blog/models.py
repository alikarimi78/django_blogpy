from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    content = RichTextField()
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    category = models.CharField(max_length=128, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

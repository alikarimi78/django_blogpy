from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
from django.contrib.auth.models import User
from django import forms
from ckeditor.widgets import CKEditorWidget


class Article(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    content = RichTextField()
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    category = models.CharField(max_length=128, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'author']
        widgets = {
            'content': CKEditorWidget(),  # Use CKEditor for content field
        }

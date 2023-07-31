from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "created_at"]


admin.site.register(Article, ArticleAdmin)

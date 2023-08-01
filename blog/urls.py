from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name="index"),
    path('CreateArticle/', views.CreateArticle.as_view(), name="create_article"),
]

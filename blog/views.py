from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import *
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import ArticleSerializer, UserProfileSerializer, AdminArticleSerializer
from .exclusive_permission import IsAuthorOrAdmin
from rest_framework.permissions import IsAdminUser


class IndexPage(TemplateView):
    def get(self, request, **kwargs):
        article_data = []
        all_articles = Article.objects.all().order_by('created_at')[:2]

        for article in all_articles:
            article_data.append(
                {
                    "title": article.title,
                    "category": article.category,
                    "created_at": article.created_at,
                    "author": article.author.user.first_name,
                    "content": article.content,
                }
            )
        context = {
            "article_data": article_data
        }
        return render(request, "index.html", context)


class CreateArticle(TemplateView):
    template_name = "create_article.html"

    def get(self, request, **kwargs):
        form = ArticleForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the home page after successful form submission
        return render(request, self.template_name, {'form': form})


class ArticleCreatePIView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleListPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'
    permission_classes = (IsAuthorOrAdmin,)


class AdminUserProfileUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAdminUser,)


class AdminArticleUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = AdminArticleSerializer
    permission_classes = (IsAdminUser,)

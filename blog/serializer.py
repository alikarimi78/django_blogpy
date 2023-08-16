from rest_framework import serializers
from .models import Article, UserProfile


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ['is_admin_accepted']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class AdminArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

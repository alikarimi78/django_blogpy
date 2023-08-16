from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name="index"),
    path('CreateArticle/', views.CreateArticle.as_view(), name="create_article"),
    path('api/list', views.ArticleListPIView.as_view(), name="article-list-api-view"),
    path('api/create', views.ArticleCreatePIView.as_view(), name="article-crate-api-view"),
    path('api/rud/<int:pk>', views.ArticleRUDAPIView.as_view(), name="article-RUD-api-view"),
    path('api/admin/userprofile/<int:pk>', views.AdminUserProfileUpdateAPIView.as_view(), name="admin-profile-update"
                                                                                               "-api-view"),
    path('api/admin/article/<int:pk>', views.AdminArticleUpdateAPIView.as_view(), name="admin-article-update-api-view"),
]

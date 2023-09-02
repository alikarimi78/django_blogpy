from django.urls import path
from map import views

urlpatterns = [
    path('', views.map_page, name='OSM_page'),
    path('upload/', views.upload_tiff, name='upload_tiff'),
]
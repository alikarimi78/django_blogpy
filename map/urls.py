from django.urls import path
from map import views

urlpatterns = [
    path('', views.MapPage.as_view(), name='OSM_page')
]
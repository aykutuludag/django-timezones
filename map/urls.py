# map/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('geojson/', views.timezone_geojson, name='geojson'),
]
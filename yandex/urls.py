from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.ya_index, name='ya_index'),
    path('metrics/', views.ya_metrics, name='ya_metrics'),
]

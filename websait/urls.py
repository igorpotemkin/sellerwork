from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.web_index, name='web_index'),
    path('sales/', views.web_sales, name='web_sales'),
]

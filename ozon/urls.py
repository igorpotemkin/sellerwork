from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.ozon_index, name='ozon_index'),
    path('import_products_ozon/', views.ozon_import_products_ozon, name='import_products_ozon'),
    path('ozon_import_metrics/', views.ozon_import_metrics, name='ozon_import_metrics'),



    path('import_products_is/', views.ozon_import_products_is, name='ozon_import_products_is'),
    path('import_order_day/', views.ozon_import_order_day, name='ozon_import_order_day'),
    path('import_warehouse/', views.ozon_import_warehouse, name='ozon_import_warehouse'),


]

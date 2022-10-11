from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.wb_index, name='ozon_index'),
    path('import_products_wb/', views.wb_import_products_wb, name='wb_import_products_wb'),
    path('import_product_info/', views.wb_import_product_info, name='wb_import_product_info'),
    path('import_stock/', views.wb_import_stock, name='wb_import_stock'),
    path('import_reports/', views.wb_import_reports, name='wb_import_reports'),
    path('import_sales/', views.wb_import_sales, name='wb_import_sales'),



]

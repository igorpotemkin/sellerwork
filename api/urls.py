from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.api_index, name='api_index'),
    path('get_prod/', views.api_get_prod, name='api_get_prod'),
    path('get_stock/', views.api_get_stock, name='api_get_stock'),
    path('get_stock_order/', views.api_get_stock_order, name='api_get_stock_order'),


    path('read_exel/', views.api_read_exel, name='api_read_exel'),

    path('get_day_present/', views.api_get_day_present, name='api_get_day_present'),

    path('get_order/', views.api_get_order, name='api_get_order'),
    #+ остатки на складе маркет и рекомендаия к заказу
    path('get_stocks/', views.api_get_stocks, name='api_get_stocks'),
    path('get_reck_order/', views.api_get_reck_order, name='api_get_reck_order'),
    #- остатки на складе маркет и рекомендаия к заказу
    #- яндекс метрика
    path('get_ya_metrik/', views.api_get_ya_metrik, name='api_get_ya_metrik'),
    #- яндекс метрика
    #+ сайт
    path('get_sait_info/', views.api_get_sait_info, name='api_get_sait_info'),
    #- сайт

    path('info_ecom/', views.api_info_ecom, name='api_info_ecom'),

    path('parsing_files/<str:files>&<str:key>&<str:ec>', views.api_parsing_files, name='api_parsing_files'),
    path('get_key_word/', views.api_get_key_word, name='api_get_key_word'),






]

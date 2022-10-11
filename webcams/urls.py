from django.conf.urls.static import static
from django.urls import path, re_path

from seller_work import settings
from . import views

urlpatterns = [

    path('start/', views.cams_start, name='cams_start'),
    path('cams_get_list/<str:order>', views.cams_get_list, name='cams_get_list'),
    path('cams_del/', views.cams_del, name='cams_del'),
    path('', views.cams_index, name='cams_index'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



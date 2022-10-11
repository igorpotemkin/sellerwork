from django.shortcuts import render
import requests
import time
from datetime import datetime, timedelta, date
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from api import models as api_models
from .service import products,metrics,stock

#Хлебокомбинат
#id = 3
header_params_h = {
    'Content-Type': 'application/json',
    'Host': 'api-seller.ozon.ru',
    'Client-Id': '8075',
    'Api-Key': '1e5fadf9-4d4b-4eb7-bf28-a58c7e7064fc'
}
#Смартбар
#id = 2
header_params_s = {
    'Content-Type': 'application/json',
    'Host': 'api-seller.ozon.ru',
    'Client-Id': '446315',
    'Api-Key': '9a38ddc2-d6b7-47a9-8f8a-27dc8555a69c'
}
#Ип Васильев
#id = 1
header_params_i = {
    'Content-Type': 'application/json',
    'Host': 'api-seller.ozon.ru',
    'Client-Id': '446790',
    'Api-Key': 'd4b1ba6f-66c2-4152-9ad9-fd17b9c00fea'
}


def ozon_index(request):

    return HttpResponse('ok')




'''импорт товаров из озон'''
def ozon_import_products_ozon(request):
    #products.import_products_ozon(1,header_params_i)
    #products.import_products_ozon(2,header_params_s)
    products.import_products_ozon(3,header_params_h)
    return HttpResponse('ok')



'''импорт метрики'''
@csrf_exempt
def ozon_import_metrics(request):
    date_from = datetime.now() - timedelta(2)
    date_from = date_from.strftime('%Y-%m-%d')

    date_to = datetime.now() - timedelta(1)
    date_to = date_to.strftime('%Y-%m-%d')

    metrics.import_metrics_ozon(3, header_params_h, date_from, date_to)
    '''print(header_params_h)
    metrics.import_metrics_ozon(2, header_params_s, date_from, date_to)
    print(header_params_s)
    metrics.import_metrics_ozon(1, header_params_i, date_from, date_to)
    print(header_params_i)'''

    return HttpResponse('ok')




'''синхронизация товаров из 1с'''
def ozon_import_products_is(request):

    return HttpResponse('ok')
'''синхронизация товаров из 1с'''
def ozon_import_order_day(request):

    return HttpResponse('ok')


'''импорт складов'''
def ozon_import_warehouse(request):

    return HttpResponse('ok')

# Create your views here.

import json
import requests
import time
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from wb import models as wb_models
from .service import products
#Смартбар
id_s = 2
header_params_s = {
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6ImIxZjk5NDdjLTIyMzktNGE5Zi04MzViLTVlNTI4NmVlNjhkNSJ9.4jF2YY9L5dorxBAs9I1NS8wf-4bSpjXfBgvxayviFps'
}
key_s_32 = "c1cf9403-0f92-4cf7-8c69-ef2f5b461151"
key_s_64 = "YzFjZjk0MDMtMGY5Mi00Y2Y3LThjNjktZWYyZjViNDYxMTUx"

#ИП Васильев
#id = 1
header_params_i = {
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6ImIxZjk5NDdjLTIyMzktNGE5Zi04MzViLTVlNTI4NmVlNjhkNSJ9.4jF2YY9L5dorxBAs9I1NS8wf-4bSpjXfBgvxayviFps'
}
key_i_32 = "f5623e71-120b-41e1-bfd5-2b59de4498b2"
key_i_64 = "ZjU2MjNlNzEtMTIwYi00MWUxLWJmZDUtMmI1OWRlNDQ5OGIy"

#СХБ
id_h = 3
header_params_s = {
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6ImIxZjk5NDdjLTIyMzktNGE5Zi04MzViLTVlNTI4NmVlNjhkNSJ9.4jF2YY9L5dorxBAs9I1NS8wf-4bSpjXfBgvxayviFps'
}
#key_h_32 = "c1cf9403-0f92-4cf7-8c69-ef2f5b461151"
key_h_64 = "Nzg5YzhkYTktMjQ2ZC00OTgyLThkYzQtYmNjNjE5M2U0Y2Yy"


def wb_index(request):
    return True

'''импорт цен скидок ид товаров'''
def wb_import_products_wb(request):

    products.import_products_wb(2, header_params_s)

    return HttpResponse('ok')

'''импорт остатков за день'''
@csrf_exempt
def wb_import_stock(request):


    products.sales(key_h_64)
    time.sleep(10)
    products.stock(key_h_64)
    '''k = 0
    for k in range(72):

        products.stock(key_h_64)
        print('stock')
        k = k+1
        print(k)
        time.sleep(1200)'''

    return HttpResponse('ok')

'''импорт информации о товаре'''
def wb_import_product_info(request):

    return HttpResponse('ok')


def wb_import_reports(request):


    products.report(key_h_64)
    m = wb_models.sales.objects.filter(barcode='4630017466160',date__lt='2022-08-02')
    k = []
    for val in m:
        k.append(val.forPay)

    print(sum(k))
    return HttpResponse('ok')



def wb_import_sales(request):
    products.stock(key_h_64)
    #products.sales(key_h_64)

    return HttpResponse('ok')
# Create your views here.

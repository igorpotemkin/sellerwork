import os
import shutil

import requests
import json
import pandas as pd
from seller_work.settings import MEDIA_ROOT
from django.conf import settings
import socket

'''загрузка товаров из ozona'''
def ozon_import_product():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    l = 'http://' + s.getsockname()[0] + ':8000/'
    requests.get(l + 'ozon/import_products_ozon/')
    print('gotovo!')

'''импорт метрики'''
def ozon_import_metrics():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    l = 'http://' + s.getsockname()[0] + ':8000/'
    requests.get(l + 'ozon/ozon_import_metrics/')
    print('gotovo!')



'''загрузка товаров из wb'''
def wb_import_product():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    l = 'http://' + s.getsockname()[0] + ':8000/'
    requests.get(l + 'wb/import_products_wb/')
    print('gotovo!')

def wb_import_product_info():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    l = 'http://' + s.getsockname()[0] + ':8000/'
    requests.get(l + 'wb/import_product_info/')
    print('gotovo!')

def wb_import_stock():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    l = 'http://' + s.getsockname()[0] + ':8000/'
    requests.get(l + 'wb/import_stock/')
    print('gotovo!')

def wb_reports():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    l = 'http://' + s.getsockname()[0] + ':8000/'
    requests.get(l + 'wb/import_reports/')
    print('gotovo!')

def wb_sales():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    l = 'http://' + s.getsockname()[0] + ':8000/'
    requests.get(l + 'wb/import_sales/')
    print('gotovo!')

''''''
def cron():
    ozon_import_metrics()
    '''wb'''
    wb_import_stock()
    #wb_import_product()
    #wb_import_product_info()

''''''
def read_exel_ya():
    '''s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    l = 'http://' + s.getsockname()[0] + ':8000/'
    requests.get(l + 'api/read_exel/')
    print('gotovo!')

    xl = pd.read_excel('media/files/ya/sales.xlsx', sheet_name='Товары', usecols=['День','Месяц','Год', 'ID бренда','Бренд','Ваш SKU','Название товара'
        ,'Показы','Добавлено в корзину, шт.','Продажи, шт.','Цена товара, руб.','Продажи, руб.'])
    data = pd.DataFrame(xl)

    k = 0
    l = []
    for k in range(data.index.stop):
        day = data.loc[k]['День'][:2]
        mes = data.loc[k]['Месяц'][:2]
        god = data.loc[k]['Год']
        data_sale = str(god) +'-'+str(mes)+'-'+ str(day)
        idBrand = data.loc[k]['ID бренда']
        brand = data.loc[k]['Бренд']
        sku = data.loc[k]['Ваш SKU']
        title = data.loc[k]['Название товара']
        hits_view = data.loc[k]['Показы']
        hits_tocart = data.loc[k]['Добавлено в корзину, шт.']
        ordered_units = data.loc[k]['Продажи, шт.']
        price = data.loc[k]['Цена товара, руб.']
        revenue = data.loc[k]['Продажи, руб.']
        l.append({"data_sale":str(data_sale),
                  'idBrand':idBrand,
                  'brand':brand,
                  'sku':sku,
                  'title':title,
                  'hits_view':hits_view,
                  'hits_tocart':hits_tocart,
                  'ordered_units':ordered_units,
                  'price':price,
                  'revenue':revenue })
    gf = str(l)
    datak = json.dumps(gf)

    with open("media/files/ya/sales.json","w") as jsonfile:
        json.dump(datak,jsonfile)'''

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    l = 'http://' + s.getsockname()[0] + ':8000/'
    requests.get(l + 'api/read_exel/')
    print('gotovo!')
    #os.remove('media/files/ya/sales.json')
    return 'ok'

''''''
def get_order():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    l = 'http://' + s.getsockname()[0] + ':8000/'
    requests.get(l + 'api/get_order/')
    print('gotovo!')
    return 'ok'

''''''
def copy_files_from_o():
    '''s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    l = 'http://' + s.getsockname()[0] + ':8000/'
    requests.get(l + 'api/test_o/')
    print('gotovo!')
    return 'ok
    with open("O:/_up/ozon/stocks_ozon.xlsx", "r", encoding='utf-8') as f:
        d = json.load(f)
        print(d)
    print(os.path.exists('O:/_up/ozon/stocks_ozon.xlsx'))'''

    '''ozon'''
    if os.path.exists('O:/_up/ozon/stocks_ozon.xlsx')== True:
        shutil.copy(
            os.path.join('O:/_up/ozon/', 'stocks_ozon.xlsx'),
            os.path.join('D:/project/seller_work/media/files/ozon/')
        )

    '''ya'''
    if os.path.exists('O:/_up/yandex/stocks.xlsx')== True:
        shutil.copy(
            os.path.join('O:/_up/yandex/', 'stocks.xlsx'),
            os.path.join('D:/project/seller_work/media/files/ya/')
        )

    if os.path.exists('O:/_up/yandex/sales.xlsx')== True:
        shutil.copy(
            os.path.join('O:/_up/yandex/', 'sales.xlsx'),
            os.path.join('D:/project/seller_work/media/files/ya/')
        )




if __name__ == '__main__':
    '''разовые импорты'''
    '''озон'''
    #ozon_import_product()
    '''задания по расписанию'''
    #cron()

    '''все что выше то работает'''
    #wb_import_product()
    #wb_reports()
    #wb_sales()
    #wb_import_stock()
    #import_all_product()
    #ozon_import_order()
    #import_products()
    #import_prod_info()
    #ozon_import_stocks()

    #copy_files_from_o()
    #read_exel_ya()
    wb_import_stock()
    #ozon_import_metrics()

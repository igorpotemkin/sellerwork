import pandas as pd
import json
from django.conf import settings
import openpyxl
from django.conf.urls.static import static
from datetime import datetime

from django.http import HttpResponse

from yandex import models as ya_model
from ozon import models as ozon_model

'''yandex'''
def read_sales_ya():

    xl = pd.read_excel(settings.MEDIA_ROOT+'\ya\sales.xlsx', sheet_name='Товары', usecols=['День','Месяц','Год', 'ID бренда','Бренд','Ваш SKU','Название товара'
        ,'Показы','Добавлено в корзину, шт.','Продажи, шт.','Цена товара, руб.','Продажи, руб.'])
    data = pd.DataFrame(xl)

    k = 0
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
        ya = ya_model.sales.objects.update_or_create(data_sale=data_sale,sku=sku,defaults={"data_sale":data_sale,
                                                                                           "idBrand":idBrand,
                                                                                           "brand":brand,
                                                                                           "sku":sku,
                                                                                           "title":title,
                                                                                           "hits_view":hits_view,
                                                                                           "hits_tocart":hits_tocart,
                                                                                           "ordered_units":ordered_units,
                                                                                           "price":price,
                                                                                           "revenue":revenue})






    return 'ok'

def read_stock_ya():
    xl = pd.read_excel(settings.MEDIA_ROOT+'\ya\stocks.xlsx', sheet_name='Лист1',usecols=['Ваш SKU',
                                                                                          'Название товара',
                                                                                          'Доступно для заказа',
                                                                                          'Склад'])
    data = pd.DataFrame(xl)
    k = 0
    dateFrom = datetime.now()
    dateFrom = dateFrom.strftime('%Y-%m-%d')
    for k in range(data.index.stop):
        if len(str(data.loc[k]['Название товара'])) > 10:
            sku = data.loc[k]['Ваш SKU']
            title = data.loc[k]['Название товара']
            units = data.loc[k]['Доступно для заказа']
            warehouse = data.loc[k]['Склад']
            print(warehouse)
            try:
                ya = ya_model.stocks.objects.update_or_create(dataparsing=dateFrom,sku=sku,warehouse=warehouse,defaults={"sku":sku,
                                                                                                   "title":title,
                                                                                                   "units":units,
                                                                                                   "sku":sku,
                                                                                                   "warehouse":warehouse})
            except:
                print(sku)
    return HttpResponse('ok')

''' end yandex'''
def read_stock_ozon():
    sheets = pd.ExcelFile(settings.MEDIA_ROOT + '\ozon\stocks_ozon.xlsx')

    for val in sheets.sheet_names:
        if val != "Итого":
            print(val)
            xl = pd.read_excel(settings.MEDIA_ROOT + '\ozon\stocks_ozon.xlsx', sheet_name=str(val),usecols=['OZON SKU ID',
                                                                                                                    'Наименование товара',
                                                                                                                    'Категория товара',
                                                                                                                    'Доступно к продаже всего, шт'])
            data = pd.DataFrame(xl)
            k = 0
            dateFrom = datetime.now()
            dateFrom = dateFrom.strftime('%Y-%m-%d')
            for k in range(data.index.stop):
                sku = data.loc[k]['OZON SKU ID']
                title = data.loc[k]['Наименование товара']
                brand = data.loc[k]['Категория товара']
                present = data.loc[k]['Доступно к продаже всего, шт']
                warehouse = str(val)

                try:
                    oz = ozon_model.ozon_stock_warehouse.objects.update_or_create(dataparsing=dateFrom,sku=sku,warehouse=warehouse,defaults={"dataparsing":dateFrom,
                                                                                                                         "sku":sku,
                                                                                                                         "title":title,
                                                                                                                         "brand":brand,
                                                                                                                         "present":present,
                                                                                                                         #"dataparsing":"2022-08-25",
                                                                                                                         "warehouse":warehouse})
                except:
                    print(sku)
                    print(title)
                    print(brand)
                    print(present)
                    print(warehouse)

    return True
    #print(data.loc(0)['Артикул продавца'])
    #print(data.loc(0)['Доступно к продаже всего, шт'])


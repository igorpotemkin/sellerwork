import json
import requests

from datetime import datetime, date, timedelta
from django.utils.timezone import now
from api import models as api_models
from wb import models as wb_models

'''start cron'''
def stock(key):
    date_from = datetime.now()
    date_from = date_from.strftime('%Y-%m-%d')

    url = "https://suppliers-stats.wildberries.ru/api/v1/supplier/stocks?key="+key+"&dateFrom="+date_from
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.text

    with open("media/files/wb/stock"+date_from+".json", "w", encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False)

    date_from = datetime.now()
    date_from = date_from.strftime('%Y-%m-%d')


    with open("media/files/wb/stock"+date_from+".json", "r", encoding='utf-8') as f:
        d = json.load(f)
        datakey = json.loads(d)
        for key in datakey:
            print(key['nmId'])
            print(key['warehouseName'])
            w = wb_models.stock.objects.update_or_create(nmId=key['nmId'],dataparsing=date_from,warehouse=key['warehouse'],defaults={"barcode":key['barcode'],
                                                                                          "quantity": key['quantity'],
                                                                                          "warehouse": key['warehouse'],
                                                                                          "warehouseName": key['warehouseName'],
                                                                                          "nmId": key['nmId'],
                                                                                          "subject": key['subject'],
                                                                                          "brand": key['brand'],
                                                                                          "subject": key['subject'],
                                                                                          "Price": key['Price'],
                                                                                          "Discount": key['Discount']})
def sales(key):
    dateFrom = datetime.now() - timedelta(5)
    dateFrom = dateFrom.strftime('%Y-%m-%d')



    url = "https://suppliers-stats.wildberries.ru/api/v1/supplier/sales?dateFrom="+dateFrom+"&flag=0&key="+key

    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.text

    with open("media/files/wb/sales"+dateFrom+".json","w", encoding='utf-8') as jsonfile:
        json.dump(data,jsonfile,ensure_ascii=False)
    l = []
    with open("media/files/wb/sales"+dateFrom+".json", "r", encoding='utf-8') as f:
        d = json.load(f)
        datakey = json.loads(d)
        for key in datakey:
            s = wb_models.sales.objects.update_or_create(saleID=key['saleID'], defaults={'saleID': key['saleID'],
                                                                                         'date': key['date'][:10],
                                                                                         'lastChangeDate': key['lastChangeDate'][:10],
                                                                                         'supplierArticle': key['supplierArticle'],
                                                                                         'barcode': key['barcode'],
                                                                                         'totalPrice': key['totalPrice'],
                                                                                         'discountPercent': key[ 'discountPercent'],
                                                                                         'warehouseName': key['warehouseName'],
                                                                                         'forPay': key['forPay'],
                                                                                         'finishedPrice': key['finishedPrice'],
                                                                                         'priceWithDisc': key['priceWithDisc'],
                                                                                         'nmId': key['nmId'], })
    return 'ok'

'''end cron'''


def import_products_wb(org,headers):
    url = "https://suppliers-api.wildberries.ru/public/api/v1/info"
    payload = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    res = response.json()
    org = api_models.organization.objects.get(pk=org).pk
    with open("import_products_wb.json", "w", encoding='utf-8') as jsonfile:
        json.dump(res, jsonfile, ensure_ascii=False)

    for key in res:
        m = wb_models.wb_info.objects.update_or_create(nmId=key['nmId'],defaults={"nmId":key['nmId'],
                                                                                  "price": key['price'],
                                                                                  "discount": key['discount'],
                                                                                  "promocode": key['promoCode'],
                                                                                  "org": org})
        print(key['nmId'])
    return True

def import_products_info_wb(org,headers):
    url = "https://suppliers-api.wildberries.ru/card/list"
    payload = json.dumps({
        "id": 1,
        "jsonrpc": "2.0",
        "params": {
            "query": {
              "limit": 1000,
              "offset": 0,#отступ с начала
              "total": 0,
            },
        }
    })
    response = requests.request("POST", url, headers=headers, data=payload)

    d = response.json()
    with open("import_products_info_wb.json", "w", encoding='utf-8') as jsonfile:
        json.dump(d, jsonfile, ensure_ascii=False)

    '''for key in d['result']['cards']:
        object = key['object']
        for addin in key['addin']:
            if addin['type'] == 'Бренд':
                brand = addin['params'][0]['value']

        for nomenk in key['nomenclatures']:
            nmId = nomenk['nmId']
            vendorCode = nomenk['vendorCode']
            for bar in nomenk['variations']:
                if len(bar['barcodes']) > 0:
                    barcode = bar['barcodes'][0]
                else:
                    barcode = ''


        try:
            info_pk = wb_models.wb_info.objects.get(nmId=nmId)
            wbprod = wb_models.wb_products_info.objects.update_or_create(info=info_pk,defaults={"info":info_pk,
                                                                                                "object":object,
                                                                                                "brand":brand,
                                                                                                "vendorCode":vendorCode,
                                                                                                "barcode":barcode,
                                                                                                })
        except:
            False
        print(key['nmId'])'''

    return True




def report(key):
    dateFrom = datetime.now() - timedelta(2)
    dateFrom = dateFrom.strftime('%Y-%m-%d')



    url = "https://suppliers-stats.wildberries.ru/api/v1/supplier/sales?dateFrom="+dateFrom+"&flag=0&key="+key

    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.text

    with open("sales.json","w", encoding='utf-8') as jsonfile:
        json.dump(data,jsonfile,ensure_ascii=False)
    '''l = []
    with open('sales.json', "r", encoding='utf-8') as f:
        d = json.load(f)
        #datakey = json.loads(d)
        for key in d:

            s = wb_models.sales.objects.update_or_create(saleID=key['saleID'],defaults={'saleID':key['saleID'],
                                                                                        'date':key['date'][:10],
                                                                                        'lastChangeDate':key['lastChangeDate'][:10],
                                                                                        'supplierArticle':key['supplierArticle'],
                                                                                        'barcode':key['barcode'],
                                                                                        'totalPrice':key['totalPrice'],
                                                                                        'discountPercent':key['discountPercent'],
                                                                                        'warehouseName':key['warehouseName'],
                                                                                        'forPay':key['forPay'],
                                                                                        'finishedPrice':key['finishedPrice'],
                                                                                        'priceWithDisc':key['priceWithDisc'],
                                                                                        'nmId':key['nmId'],})'''




    return 'ok'
    #return response.status_code


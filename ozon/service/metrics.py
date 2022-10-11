import json
import requests
from datetime import datetime, date
from api import models as api_models
from ozon import models as ozon_models
def import_metrics_ozon(org,headers,data_from,data_to):
    '''
    hits_view — всего показов,
    hits_tocart — всего добавлено в корзину,
    revenue — заказано на сумму,
    returns — возвращено товаров,
    ordered_units — заказано товаров,
    cancellations — отменено товаров,
    conv_tocart — общая конверсия в корзину,
    '''
    l = {"date_from": data_from,
         "date_to":data_to,
         "metrics":["hits_view","hits_tocart","revenue","returns","ordered_units","cancellations","conv_tocart"],
         "dimension": ["sku", "day"],
         "limit": 500,
         "offset": 0
         }
    url = 'https://api-seller.ozon.ru/v1/analytics/data'
    data = json.dumps(l)

    get_req = requests.post(url, data=data, headers=headers)
    try:
        result = get_req.json()
        org = api_models.organization.objects.get(pk=org).pk
        for key in result['result']['data']:
            sku = key['dimensions'][0]['id']
            datapar = key['dimensions'][1]['id']
            try:
                p = ozon_models.prod_ozon.objects.get(sku=sku,org=org)
                try:
                    pr,m = ozon_models.metrics_ozon.objects.update_or_create(product=p,dataparsing=datapar,org=org,defaults={"product":p,
                                                                                                                          "org":org,
                                                                                                                          "dataparsing":datapar,
                                                                                                                          "hits_view":key['metrics'][0],
                                                                                                                          "hits_tocart":key['metrics'][1],
                                                                                                                          "revenue":key['metrics'][2],
                                                                                                                          "returns":key['metrics'][3],
                                                                                                                          "ordered_units":key['metrics'][4],
                                                                                                                          "cancellations":key['metrics'][5],
                                                                                                                          "conv_tocart":key['metrics'][6]
                                                                                                                          })
                    '''импорт остатков за день'''
                    ozon_getStockById(p.pk, str(p.product_id), str(p.offer_id),headers)
                    import_price(p.pk, str(p.product_id), str(p.offer_id),headers)
                except:
                    False

            except:
                    False
    except:
        print('error')





def ozon_getStockById(pk,prod_id,off_id,headers):
    offer_id = []
    offer = off_id.encode('utf-8', 'replace')
    off = offer.decode('utf-8', 'replace')
    offer_id.append(off)
    product_id = []
    prodid = prod_id.encode('utf-8', 'replace')
    prodid = prodid.decode('utf-8', 'replace')
    product_id.append(prodid)
    l = {"filter": {"offer_id": offer_id,
                    "product_id": product_id,
                    "visibility": "ALL"},
         "last_id": "", "limit": 100}

    url = 'https://api-seller.ozon.ru/v3/product/info/stocks'

    data = json.dumps(l)

    get_req = requests.post(url, data=data, headers=headers)
    result = get_req.json()
    p = ozon_models.prod_ozon.objects.get(pk=pk)

    res={}
    for key in result['result']['items']:
        for val in key['stocks']:
            if val['type'] == 'fbo':
                default_val={"product":p,
                             "dataparsing":date.today(),
                             "type":val['type'],
                             "present":val['present'],
                             "reserved":val['reserved']
                             }
                pi,pinfo = ozon_models.ozon_stocks.objects.update_or_create(product=p,dataparsing=date.today(),defaults=default_val)


    return res

def import_price(pk,prod_id,off_id,headers):

    res = {}

    offer_id = []
    offer = off_id.encode('utf-8', 'replace')
    off = offer.decode('utf-8', 'replace')
    offer_id.append(off)
    product_id = []
    prodid = prod_id.encode('utf-8', 'replace')
    prodid = prodid.decode('utf-8', 'replace')
    product_id.append(prodid)
    l = {"filter": {"offer_id": offer_id,
                    "product_id": product_id,
                    "visibility": "ALL"},
         "last_id": "", "limit": 100}

    url = 'https://api-seller.ozon.ru/v4/product/info/prices'
    data = json.dumps(l)

    get_req = requests.post(url, data=data, headers=headers)
    result = get_req.json()

    with open("price_ozon.json", "w", encoding='utf-8') as jsonfile:
        json.dump(result, jsonfile, ensure_ascii=False)

    return res
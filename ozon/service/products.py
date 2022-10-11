import json
import requests
from api import models as api_models
from ozon import models as ozon_models

def import_products_ozon(org,headers):
    l ={"filter": {"offer_id": [],"product_id": [],"visibility": "ALL" },"last_id": "","limit": 500}

    url = 'http://api-seller.ozon.ru/v2/product/list'
    data = json.dumps(l)

    get_req = requests.post(url, data=data, headers=headers)
    result = get_req.json()
    json_object = result['result']['items']

    org = api_models.organization.objects.get(pk=org)
    for val in json_object:

        sk = ozon_getInfoById(val['product_id'], val['offer_id'],headers)
        pr, prod = ozon_models.prod_ozon.objects.update_or_create(product_id=val['product_id'], defaults={'product_id': val['product_id'],
                                                                                                'offer_id': val['offer_id'],
                                                                                                'name': sk['name'],
                                                                                                'barcode': sk['barcode'],
                                                                                                'sku': sk['fbo_sku'],
                                                                                                'org':org.pk
                                                                                                })
        #ozon_getStockById(pr.pk, str(pr.product_id), str(pr.offer_id))

'''получение всей информации о товаре по его ид
- артикул
-штрих код barcode'''
def ozon_getInfoById(product_id, offer_id,headers):

    l = {"offer_id": "",
         "product_id": product_id,
         "sku": 0}

    url = 'http://api-seller.ozon.ru/v2/product/info'
    data = json.dumps(l)

    get_req = requests.post(url, data=data, headers=headers)
    result = get_req.json()
    #json_object = json.loads(result['result'])
    json_object = result['result']
    jsres = {}

    jsres.update({'name':json_object['name'],
                  'barcode':json_object['barcode'],
                  'fbo_sku':json_object['fbo_sku']})




    return jsres
''''''





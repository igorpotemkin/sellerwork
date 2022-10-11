import json
import os

from django.utils.timezone import now
from api import models as api_models

def parser(file,key,ec):
    e = api_models.ecom.objects.get(pk=ec)
    try:
        k = api_models.keywords.objects.get(description=key)
    except:
        False

    datap = now().strftime('%Y-%m-%d')
    dir = "media/files/parser/"
    with open(dir + file, "r", encoding='utf-8') as f:
        d = json.load(f)
        if k:
            for val in d:
                default = {'keys':k,
                           'pos': val['pos'],
                           'ecom': e.pk,
                           'region': val['region'],
                           'link': val['link'],
                           'lower_price': val['lower_price'],
                           'old_price': val['old_price'],
                           'brand_name': val['brand_name'],
                           'goods_name': val['goods_name']}
                #if val['brand_name'] == 'MUSTHAVE' or val['brand_name'] == 'Musler':
                print(val['brand_name'])
                print(val['pos'])
                f = api_models.linkparser.objects.update_or_create(keys=k.pk,dataparsing=datap,link=val['link'],defaults=default)




    print('ok')
from datetime import datetime, timedelta
import json
import requests
from django.http import HttpResponse
from websait import models as web_models


def get_sale_sait():
    date_from = datetime.now() - timedelta(2)
    date_from = date_from.strftime('%Y-%m-%d')

    date_to = datetime.now() - timedelta(1)
    date_to = date_to.strftime('%Y-%m-%d')

    url = "https://smartbar.ru/api/getordersbydate/"

    payload = '{"date_from": "'+date_from+'","date_to":"'+date_to+'"}'

    headers = {
        'ApiToken': '7dQkt3gubyKrt23423sasjh665EhKp3qrYHycjgK',
        'Content-Type': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.text
    with open("media/files/site/sale.json", "w") as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False)
    with open("media/files/site/sale.json", "r", encoding='utf-8') as f:
        d = json.load(f)
        datakey = json.loads(d)
        for key in datakey['data']:
            if key["is_one_click"] == 'false':
                is_one_click = False
            else:
                is_one_click = True
            q = web_models.sales_sait.objects.create(name=key["name"],
                                                    xml_id=key["xml_id"],
                                                    quantity=key["quantity"],
                                                    order_id=key["order_id"],
                                                    order_date=key["order_date"],
                                                    is_one_click=is_one_click,
                                                    summ=key["sum"])
            #print(key)

    return HttpResponse('ok')
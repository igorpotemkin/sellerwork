from tapi_yandex_metrika import YandexMetrikaStats, YandexMetrikaLogsapi
import json
from datetime import datetime, timedelta, date
import pandas as pd
from yandex import models as ya_model
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)




def metrics():
    ACCESS_TOKEN = "y0_AgAAAABjs7XSAAhqIQAAAADO47Y2pCB31AV1R8K5fPku2_CbtBYe08Y"
    COUNTER_ID = "90075544"
    api = YandexMetrikaStats(
        access_token=ACCESS_TOKEN,
        receive_all_data=True
    )
    date_from = datetime.now() - timedelta(1)
    date_from = date_from.strftime('%Y-%m-%d')

    date_to = datetime.now() - timedelta(1)
    date_to = date_to.strftime('%Y-%m-%d')

    params = dict(
        ids=90075544,
        metrics="ym:s:users,ym:s:visits,ym:s:pageviews,ym:s:bounceRate,ym:s:pageDepth,ym:s:avgVisitDurationSeconds",
        dimensions="ym:s:date,ym:s:regionCountry, ym:s:regionArea, ym:s:regionCity",
        #sort="ym:s:date",
        group="Day",
        date1=date_from,
        date2=date_to,
        limit=100,
    )

    result = api.stats().get(params=params)
    result = result().data
    result = result[0]['data']
    # Создаем пустой dict (словать данных)
    dict_data = {}
    # Парсим исходный list формата Json в dictionary (словарь данных)
    for i in range(0, len(result) - 1):
        dict_data[i] = {
            'date': result[i]["dimensions"][0]["name"],
            'source': result[i]["dimensions"][1]["name"],
            'details': result[i]["dimensions"][2]["name"],
            'users': result[i]["metrics"][0],
            'visits': result[i]["metrics"][1],
            'pageviews': result[i]["metrics"][2],
            'bounceRate': result[i]["metrics"][3],
            'pageDepth': result[i]["metrics"][4],
            'avgVisitDurationSeconds': result[i]["metrics"][5]
        }
    for key,val in dict_data.items():
        default_value={"regionCountry":val['source'],
                       "regionArea":val['details'],
                       "visits":val['visits'],
                       "users":val['users'],
                       "pageviews":val['pageviews']}
        q = ya_model.metrics_site.objects.update_or_create(dataparsing=date_from,regionArea=val['details'],defaults=default_value)


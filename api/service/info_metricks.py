import json
from django.db.models import Sum
from ozon import models as ozon_models
from wb import models as wb_models


def metrics_period(day_start,day_end):
    l = {}

    '''metrics ozon'''
    m_ozon = ozon_models.metrics_ozon.objects.filter(dataparsing__range=(day_start,day_end)).order_by('-ordered_units')
    for keyo in m_ozon:
        prod = ozon_models.prod_ozon.objects.get(pk=keyo.product_id)
        if prod.org == 3:
            l.update({prod.pk:prod.sku})
            if len(l)>=20:
                break
        #l.append(prod.sku)
        #print(keyo['dataparsing'])
        #print(keyo.ordered_units)
        #print(keyo.dataparsing)
    r = []
    for key,val in l.items():
        k_prod = ozon_models.prod_ozon.objects.get(pk=key)
        ordered = ozon_models.metrics_ozon.objects.filter(dataparsing__range=(day_start, day_end),product_id=k_prod)
        hits_view = []
        hits_tocart = []
        ordered_units = []
        revenue = []
        cancellations = []
        for o in ordered:
            hits_view.append(o.hits_view)
            hits_tocart.append(o.hits_tocart)
            ordered_units.append(o.ordered_units)
            cancellations.append(o.cancellations)
            revenue.append(o.revenue)
        r.append({'sku':val,
                  'hits_view':sum(hits_view),
                  'hits_tocart':sum(hits_tocart),
                  'ordered_units':sum(ordered_units),
                  'cancellations':sum(cancellations),
                  'revenue':sum(revenue)})

    '''metrics wb'''




    #print(l)
    return r

'''
sku:{5,6,8}
'''
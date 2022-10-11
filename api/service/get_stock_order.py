from ozon import models as ozon_models
from wb import models as wb_models

def get_stock_order_ozon(day_start, day_end):
    kprod = []
    prod = ozon_models.prod_ozon.objects.filter(org=3)
    for p in prod:
        try:
            mod = ozon_models.ozon_stocks.objects.filter(product=p, dataparsing__range=(day_start, day_end))
            dt = []
            for val in mod:
                dt.append({'day': val.dataparsing.strftime('%Y-%m-%d %H:%M:%S'), 'present': val.present})

            modord = ozon_models.metrics_ozon.objects.filter(product=p, dataparsing__range=(day_start, day_end))

            allprod = 0
            for val in modord:
                ordered_units = val.ordered_units - val.cancellations
                allprod = allprod + ordered_units

            kprod.append({'prod': p.sku, 'ost': dt, 'order': allprod})
        except:
            print('none')
    #wb
    '''mod = wb_models.stock.objects.filter(dataparsing__range=(day_start, day_end))
    dt = []
    l = []
    for key in mod:
        l.append(key.nmId)
    unique_numbers = list(set(l))

    for val in unique_numbers:
        try:
            mod = wb_models.stock.objects.filter(nmId=val, dataparsing__range=(day_start, day_end))
            dt = []
            for valw in mod:
                dt.append({'day': valw.dataparsing.strftime('%Y-%m-%d %H:%M:%S'), 'present': valw.quantity})

            modord = wb_models.sales.objects.filter(nmId=val, date__range=(day_start, day_end))

            allprod = 0
            for kval in modord:
                #ordered_units = val.ordered_units - val.cancellations
                allprod = allprod + 1

            kprod.append({'prod': val, 'ost': dt, 'order': allprod})
        except:
            print('none')'''


    l = []
    print(kprod)
    return kprod
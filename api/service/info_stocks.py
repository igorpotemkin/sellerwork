from ozon import models as ozon_models

def stocks_period(day_start,day_end):
    r = []
    st = ozon_models.ozon_stocks.objects.filter(dataparsing=day_end)
    for val in st:
        r.append({"sku": val.product.sku, "present": val.present})

    return r
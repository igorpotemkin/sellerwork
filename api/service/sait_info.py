from websait import models as web_model
def s_inf(dstart,dend):
    l = []

    q = web_model.sales_sait.objects.filter(order_date__range=(dstart,dend))
    for val in q:
        datp = val.order_date
        datp = datp.strftime("%Y-%m-%d")
        summ = str(val.summ).replace('.',',')
        l.append({"data":datp,"xml_id":val.xml_id,"name":val.name,
                  "quantity":val.quantity,"summ":summ})


    return l
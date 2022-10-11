import json
import os
import shutil
from datetime import datetime, timedelta

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .service import info_metricks,info_stocks,get_stock_order,read_exel,parsing_files,sait_info
from websait.service import info_site
from ozon import models as ozon_models
from wb import models as wb_models
from yandex import models as ya_models
from api import models as api_models


def api_index(request):

    return HttpResponse('ok')


'''возвращаем информацию по метрики за период'''

@csrf_exempt
def api_get_prod(request):
    if request.method == 'POST':
        present = request.POST.get('present')
        strjs = json.loads(present)
        day_start = strjs['day_start']
        day_end = strjs['day_end']
        l = info_metricks.metrics_period(day_start,day_end)
    res = json.dumps(l)

    return HttpResponse(res)


'''возвращаем информацию по метрики за период'''
@csrf_exempt
def api_get_stock(request):
    if request.method == 'POST':
        present = request.POST.get('present')
        strjs = json.loads(present)
        day_start = strjs['day_start']
        day_end = strjs['day_end']
        l = info_stocks.stocks_period(day_start, day_end)
    res = json.dumps(l)

    return HttpResponse(res)


def api_info_ecom(request):

    return HttpResponse('ok')

'''def api_import_ecom(request):

    return HttpResponse('ok')'''


'''информация об остатках и продажах на озон'''
@csrf_exempt
def api_get_stock_order(request):
    if request.method == 'POST':
        kprod = []
        present = request.POST.get('present')
        strjs = json.loads(present)

        day_start = strjs['day_start']
        day_end = strjs['day_end']
        ecom = strjs['ecom']

        if ecom == 'ozon':
           kprod = get_stock_order.get_stock_order_ozon(day_start,day_end)



    return HttpResponse(str(kprod))

@csrf_exempt
def api_read_exel(request):
    '''ozon'''
    if os.path.exists('O:/_up/ozon/stocks_ozon.xlsx')== True:
        shutil.copy(
            os.path.join('O:/_up/ozon/', 'stocks_ozon.xlsx'),
            os.path.join('D:/project/seller_work/media/files/ozon/')
        )

    '''ya'''
    if os.path.exists('O:/_up/yandex/stocks.xlsx')== True:
        shutil.copy(
            os.path.join('O:/_up/yandex/', 'stocks.xlsx'),
            os.path.join('D:/project/seller_work/media/files/ya/')
        )

    if os.path.exists('O:/_up/yandex/sales.xlsx')== True:
        shutil.copy(
            os.path.join('O:/_up/yandex/', 'sales.xlsx'),
            os.path.join('D:/project/seller_work/media/files/ya/')
        )

    read_exel.read_sales_ya()
    read_exel.read_stock_ya()
    read_exel.read_stock_ozon()
    return HttpResponse('ok')

@csrf_exempt
def api_get_day_present(request):
    l = {}
    if request.method == 'POST':
        present = request.POST.get('present')
        strjs = json.loads(present)
        day_start = strjs['day_start']
        day_end = strjs['day_end']
        r = []

        m_ozon = ozon_models.metrics_ozon.objects.filter(dataparsing__range=(day_start,day_end)).order_by('-ordered_units')
        for keyo in m_ozon:
            prod = ozon_models.prod_ozon.objects.get(pk=keyo.product_id)
            if prod.org == 3:
                l.update({prod.pk:prod.sku})
                '''if len(l)>=20:
                    break'''
        
        for key,val in l.items():
            k_prod = ozon_models.prod_ozon.objects.get(pk=key)
            ordered = ozon_models.metrics_ozon.objects.filter(dataparsing__range=(day_start, day_end),product_id=k_prod)
            for o in ordered:
                datp = o.dataparsing
                datp = datp.strftime("%Y-%m-%d")
                r.append({'sku':val,
                          'day':datp,
                          'hits_view':o.hits_view,
                          'hits_tocart':o.hits_tocart,
                          'ordered_units':o.ordered_units,
                          'cancellations':o.cancellations,
                          'revenue':o.revenue})



        '''wb'''
        m_wb = wb_models.sales.objects.filter(date__range=(day_start,day_end))

        for keyw in m_wb:
            datp = keyw.date
            datp = datp.strftime("%Y-%m-%d")
            #print(str(keyw.forPay))
            r.append({'sku': str(keyw.nmId),
                      'day': datp,
                      'hits_view': 0,
                      'hits_tocart': '',
                      'ordered_units': 1,#заказано товаров
                      'cancellations': '',
                      'revenue': str(keyw.forPay)})#заказано на сумму

        '''yandex'''
        m_wb = ya_models.sales.objects.filter(data_sale__range=(day_start,day_end))

        for keyw in m_wb:
            datp = keyw.data_sale
            datp = datp.strftime("%Y-%m-%d")
            #print(str(keyw.forPay))
            r.append({'sku': str(keyw.sku),
                      'day': datp,
                      'hits_view': keyw.hits_view,
                      'hits_tocart': keyw.hits_tocart,
                      'ordered_units': keyw.ordered_units,#заказано товаров
                      'cancellations': '',
                      'revenue': str(keyw.revenue)})#заказано на сумму






    return HttpResponse(str(r))


def api_get_order(request):
    m = wb_models.sales.objects.filter(barcode='4630017466160',date__range=('2022-08-01','2022-08-02'))
    k = []
    for val in m:
        k.append(val.forPay)

    #print(sum(k))
    return HttpResponse('ok')

@csrf_exempt
def api_get_stocks(request):

    if request.method == 'POST':
        present = request.POST.get('present')
        strjs = json.loads(present)
        day_start = strjs['day_start']
        day_end = strjs['day_end']
        #print(day_start)
        #print(day_end)
        r = []

        '''ozon'''

        oz = ozon_models.ozon_stock_warehouse.objects.filter(dataparsing = day_end)
        mos = []
        reg = []
        for val in oz:
            if val.warehouse=='Хоругвино':
                r.append({'sklad':'mos','sku':val.sku,'present':int(val.present)})
            else:
                r.append({'sklad':'reg','sku':val.sku,'present':int(val.present)})

        '''wb'''

        wb = wb_models.stock.objects.filter(dataparsing=day_end)
        mos = []
        reg = []
        for val in wb:
            if val.warehouseName=='Электросталь' or val.warehouseName=='Коледино':
                r.append({'sklad':'mos','sku':val.nmId,'present':val.quantity})
            else:
                r.append({'sklad':'reg','sku':val.nmId,'present':val.quantity})

        '''ya'''

        oz = ya_models.stocks.objects.filter(dataparsing=day_end)
        mos = []
        reg = []
        for val in oz:
            if val.warehouse=='Софьино (кроме КГТ)':
                r.append({'sklad':'mos','sku':val.sku,'present':val.units})
            else:
                r.append({'sklad':'reg','sku':val.sku,'present':val.units})
        #print(r)
    return HttpResponse(str(r))

@csrf_exempt
def api_get_reck_order(request):

    if request.method == 'POST':
        present = request.POST.get('present')
        strjs = json.loads(present)
        day_start = strjs['day_start']
        day_end = strjs['day_end']
        dtst = datetime.strptime(str.replace(day_start,'-',''), '%Y%m%d')#дата старта
        dtend = datetime.strptime(str.replace(day_end,'-',''), '%Y%m%d')#дата старта

        count_day = dtend-dtst
        #print(count_day.days)

        r = []
        ozlist = []
       #рекомедация к заказам
        '''ozon'''
        k = 0
        ozonstock = ozon_models.ozon_stocks.objects.filter(dataparsing__range=(day_start,day_end)).order_by('dataparsing')
        for val in ozonstock:
            ozlist.append(val.product.sku)
        l_oz = set(ozlist)
        for val in l_oz:
            col_day_pres = 0
            pres = 0
            pr = []

            for k in range(count_day.days+1):
                daysearch = dtst + timedelta(k)
                days = daysearch.strftime('%Y-%m-%d')
                try:
                    prodozon = ozon_models.prod_ozon.objects.get(sku=val)
                    try:
                        ozst = ozon_models.ozon_stocks.objects.filter(product=prodozon,dataparsing=days)[:1]

                        col_day_pres = col_day_pres + 1
                    except:
                        False
                except:
                    False

                try:
                    prodozon = ozon_models.prod_ozon.objects.get(sku=val)
                    ozst = ozon_models.metrics_ozon.objects.filter(product=prodozon, dataparsing=days)[:1]

                    for v in ozst:
                        pr.append(int(v.ordered_units))

                except:
                    False

                try:
                    prodstock = ozon_models.prod_ozon.objects.get(sku=val)
                    st = ozon_models.ozon_stocks.objects.get(product=prodstock, dataparsing=day_end)
                    stock = st.present
                except:
                    stock = 0

            #print(val)

            r.append({'sku_rek': val, 'present_rek': round(sum(pr)/col_day_pres*28),'present_ost':stock})

        '''wb'''
        k = 0
        wblist = []
        wbstock = wb_models.stock.objects.filter(dataparsing__range=(day_start,day_end)).order_by('dataparsing')
        for val in wbstock:
            wblist.append(val.nmId)
        l_wb = set(wblist)
        tt = []
        for val in l_wb:
            col_day_pres = 0
            pres = 0
            pr = []
            for k in range(count_day.days+1):
                daysearch = dtst + timedelta(k)
                days = daysearch.strftime('%Y-%m-%d')
                try:
                    wb = wb_models.stock.objects.filter(nmId=val,dataparsing=days)[:1]
                    col_day_pres = col_day_pres + 1
                except:
                    False

                try:
                    wbsal = wb_models.sales.objects.filter(nmId=val, date=days)
                    for v in wbsal:
                        pr.append(1)

                except:
                    False

            try:
                prodstock = wb_models.stock.objects.get(nmId=val,dataparsing=day_end)

                #print(prodstock.quantity)
                stock = prodstock.quantity
                tt.append(stock)
            except:
                stock = 0
            r.append({'sku_rek': val, 'present_rek': round(sum(pr)/col_day_pres*28),'present_ost':stock})

        '''ya'''
        k = 0
        yalist = []
        yastock = ya_models.stocks.objects.filter(dataparsing__range=(day_start,day_end)).order_by('dataparsing')
        for val in yastock:
            yalist.append(val.sku)
        l_ya = set(yalist)
        for val in l_ya:
            col_day_pres = 0
            pres = 0
            pr = []
            for k in range(count_day.days+1):
                daysearch = dtst + timedelta(k)
                days = daysearch.strftime('%Y-%m-%d')
                try:
                    ya = ya_models.stocks.objects.filter(sku=val,dataparsing=days)[:1]
                    col_day_pres = col_day_pres + 1
                except:
                    False

                try:
                    yasal = ya_models.sales.objects.filter(sku=val, data_sale=days)
                    for v in yasal:
                        pr.append(v.ordered_units)

                except:
                    False
            try:
                prodstock = ya_models.stocks.objects.filter(sku=val,dataparsing=day_end)
                stock = prodstock.units
            except:
                stock = 0

            r.append({'sku_rek': val, 'present_rek': round(sum(pr)/col_day_pres*28),'present_ost':stock})



    return HttpResponse(str(r))


@csrf_exempt
def api_get_key_word(request):
    k = api_models.keywords.objects.all()
    t = []
    for val in k:
        t.append(val.description)
    res = json.dumps(t)

    return HttpResponse(str(res))

@csrf_exempt
def api_get_ya_metrik(request):
    r = []
    present = request.POST.get('present')
    strjs = json.loads(present)
    day_start = strjs['day_start']
    day_end = strjs['day_end']
    m = ya_models.metrics_site.objects.filter(dataparsing__range=(day_start, day_end))
    for val in m:
        datp = val.dataparsing
        datp = datp.strftime("%Y-%m-%d")
        r.append({'day': datp, 'regionCountry': val.regionCountry,
                  'regionArea': val.regionArea,
                  'visits': val.visits,
                  'users': val.users,
                  'pageviews': val.pageviews})

    return HttpResponse(str(r))

@csrf_exempt
def api_parsing_files(request,files,key,ec):

    parsing_files.parser(files,key,ec)

    return HttpResponse('ok')

@csrf_exempt
def api_get_sait_info(request):
    r = []
    if request.method == 'POST':
        present = request.POST.get('present')
        strjs = json.loads(present)
        day_start = strjs['day_start']
        day_end = strjs['day_end']
        r = sait_info.s_inf(day_start,day_end)

    return HttpResponse(str(r))




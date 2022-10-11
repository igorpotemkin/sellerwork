from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
import time
import os
from .service import screen
from webcams import models as cam_models
@csrf_exempt
def cams_index(request):

    return HttpResponse('ok')

@csrf_exempt
def cams_start(request):

    if request.method == 'POST':
        ord =request.POST.get('present')
        order = json.loads(ord)

        #screen.screen_shot('rtsp://admin:Aa123456@192.168.55.80/H264?ch=1&subtype=0',1,order['order'])
        #time.sleep(5)
        screen.screen_shot('rtsp://admin:Aa123456@192.168.55.78/H264?ch=1&subtype=0',2,order['order'])
        print(order['order'])
        time.sleep(1)
        screen.screen_shot('rtsp://admin:Qq1256Qq@192.168.55.85/H264?ch=1&subtype=0',3,order['order'])
        print(order['order'])
        #screen.screen_shot('rtsp://admin:Aa123456@192.168.55.78/H264?ch=1&subtype=0')
    return HttpResponse('ok')


@csrf_exempt
def cams_get_list(request,order):
    '''if request.method == 'POST':
        ord =request.POST.get('present')
        order = json.loads(ord)
        print(order['order'])'''
    print(order)
    return render(request, 'webcams/foto_list.html',{'order':order})


@csrf_exempt
def cams_del(request):
    if request.method=='POST':
        pkc = request.POST.get('pk')
        c = cam_models.foto_order.objects.get(pk=pkc)
        if os.path.isfile(c.link):
            os.remove(c.link)

        c.delete()

    return HttpResponse('ok')

@csrf_exempt
def cams_add_othe(request):
    return HttpResponse('')


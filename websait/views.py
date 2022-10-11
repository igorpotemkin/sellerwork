from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .service import info_site


@csrf_exempt
def web_index(request):
    return HttpResponse('ok')


@csrf_exempt
def web_sales(request):
    info_site.get_sale_sait()
    return HttpResponse('ok')

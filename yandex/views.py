from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .service import metrics


def ya_index(request):
    return HttpResponse('ok')

@csrf_exempt
def ya_metrics(request):

    metrics()

    return HttpResponse('ok')
# Create your views here.

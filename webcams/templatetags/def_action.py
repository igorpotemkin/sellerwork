from django import template
from django.shortcuts import render
from datetime import datetime, timedelta, date
from webcams import models as cam_models
register = template.Library()
'''profil'''


@register.simple_tag
def get_list_files(id):
    l = {}
    c = cam_models.foto_order.objects.filter(order=id)
    for val in c:
        l.update({val.pk:val.link})
    return l
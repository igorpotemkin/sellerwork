import os
import shutil

import requests
import json
import pandas as pd
from seller_work.settings import MEDIA_ROOT
from django.conf import settings
import socket

'''загрузка товаров из ozona'''
def metrics():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    l = 'http://' + s.getsockname()[0] + ':8000/'
    requests.get(l + 'yandex/metrics/')
    print('gotovo!')


if __name__ == '__main__':
    metrics()

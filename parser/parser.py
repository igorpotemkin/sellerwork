import os
import time
import json
import socket
import requests
import re
import selenium
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


'''
Протеиновый батончик
Злаковый батончик
Батончик мюсли
Ореховый батончик
'''
qwery1 = 'Протеиновый батончик'
qwery2 = 'Злаковый батончик'
qwery3 = 'Батончик мюсли'
qwery4 = 'Ореховый батончик'
def init_driver():
    driver = webdriver.Chrome()
    driver.wait = WebDriverWait(driver, 5)
    return driver


def wb_search(qwery):
    driver = init_driver()
    driver.get('https://www.wildberries.ru/catalog/0/search.aspx?sort=popular&search='+qwery)
    time.sleep(90)
    t = []
    try:
        atrh = driver.find_elements(By.CLASS_NAME,'product-card__wrapper')
        k = 1
        for val in atrh:
            link = val.find_element(By.TAG_NAME,'a').get_attribute('href')
            lower_price = val.find_element(By.CLASS_NAME,'lower-price').text
            brand_name = val.find_element(By.CLASS_NAME,'brand-name').text
            goods_name = val.find_element(By.CLASS_NAME,'goods-name').text
            old_price = val.find_element(By.TAG_NAME,'del').text
            t.append({'pos':k,'region':'Владимир','link':link,'lower_price':lower_price,'old_price':old_price,'brand_name':brand_name,'goods_name':goods_name})
            k = k+1

    except:
        False

    dir = "../media/files/parser/"
    with open(dir+"parser_wb.json", "w", encoding='utf-8') as jsonfile:
        json.dump(t, jsonfile, ensure_ascii=False)

    driver.close()

def wb_parser():
    key = get_key_word()
    for val in key:
        if os.path.isfile(filewb):
            os.remove(filewb)
            print("success")
        else:
            print("File doesn't exists! " + val)
        wb_search(val)
        time.sleep(60)
        parsing_files("parser_wb.json",val,str(3))

    print('------------------')

def parsing_files(file,key,ec):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    l = 'http://' + s.getsockname()[0] + ':8000/'
    requests.get(l + 'api/parsing_files/'+file+'&'+key+'&'+ec)
    print('gotovo!')
    return 'ok'


def get_key_word():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    l = 'http://' + s.getsockname()[0] + ':8000/'
    k = requests.get(l + 'api/get_key_word/')

    return k.json()

def ozon_parser():
    key = get_key_word()
    for val in key:
        if os.path.isfile(file_ozon):
            os.remove(file_ozon)
            print("success")
        else:
            print("File doesn't exists! " + val)
        ozon_search(val)
        time.sleep(60)
        parsing_files("parser_ozon.json", val,str(2))

    return 'ok'

def ozon_search(qwery):
    driver = init_driver()
    driver.get('https://www.ozon.ru/category/sportivnoe-pitanie-11650/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text='+qwery)
    time.sleep(15)
    t = []
    try:
        atrh = driver.find_elements(By.CLASS_NAME,'k1p')
        k = 1
        for val in atrh:
            try:
                link = val.find_element(By.TAG_NAME,'a').get_attribute('href')
            except:
                link = ""
            try:
                lower_price = val.find_element(By.CLASS_NAME,'ui-o0').text
                lower_price = re.sub("\D", "", lower_price)
            except:
                lower_price = ''

            try:
                old_price = val.find_element(By.CLASS_NAME, 'ui-o9').text
                old_price = re.sub("\D", "", old_price)
            except:
                old_price = ''
            try:
                goods_name = val.find_element(By.CLASS_NAME,'tsBodyL').text
            except:
                goods_name = ''
            try:
                brand_name = val.find_element(By.CLASS_NAME,'ok5').text
                brand_name = brand_name.split('продавец ')
                brand_name = brand_name[1]
            except:
                brand_name = ''
            t.append({'pos':k,'region':'Владимир','link':link,'lower_price':lower_price,'old_price':old_price,'brand_name':brand_name,'goods_name':goods_name})
            k = k+1
    except:
        print('none')
        False
    print(t)
    dir = "../media/files/parser/"
    with open(dir+"parser_ozon.json", "w", encoding='utf-8') as jsonfile:
        json.dump(t, jsonfile, ensure_ascii=False)
    time.sleep(600)
    driver.close()
    return 'ok'

'''firefox'''
def init_driver_firefox():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver


def ya_parser():
    key = get_key_word()
    for val in key:
        if os.path.isfile(file_ya):
            os.remove(file_ya)
            print("success")
        else:
            print("File doesn't exists! " + val)

        ya_search(val)
        #parsing_files("parser_ya.json", val,str(2))

    return 'ok'

def ya_search(qwery):
    driver = init_driver_firefox()
    #time.sleep(60)
    driver.get('https://market.yandex.ru/')

    capch = driver.find_elements(By.CLASS_NAME,'CheckboxCaptcha-Button')
    for v in capch:
        try:
            v.click()
            time.sleep(10)
            search = driver.find_element(By.ID, 'header-search')
            search.send_keys(qwery+'\n')
            time.sleep(5)
            try:
                search.send_keys(Keys.ENTER)
            except:
                print('none')
        except:
            False
        time.sleep(300)


    t = []

    return 'ok'

if __name__ == '__main__':
    filewb = "../media/files/parser/parser_wb.json"
    file_ozon = "../media/files/parser/parser_ozon.json"
    file_ya = "../media/files/parser/parser_ya.json"
    '''k = 0
    for k in range(72):
        wb_parser()
        time.sleep(1800)'''
    #wb_parser()
    ozon_parser()
    #ya_parser()


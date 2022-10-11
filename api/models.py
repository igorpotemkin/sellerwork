from django.db import models
from django.utils.timezone import now


'''смарт бар, васильев, схб'''
class organization(models.Model):
    ref = models.CharField(max_length=36, unique=True)
    description = models.CharField(max_length=250)

'''ozon, wb и тд'''
class ecom(models.Model):
    code = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    ref = models.CharField(max_length=36,unique=True)
    delete = models.BooleanField(default=False)

class nomenklature(models.Model):
    partref = models.ForeignKey(ecom,on_delete=models.CASCADE)
    articul = models.CharField(max_length=100)
    shtrih = models.CharField(max_length=300)
    ref = models.CharField(max_length=36)
    parentref = models.CharField(max_length=36)
    lider = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)
# Create your models here.

'''table parsing'''
class keywords(models.Model):
    description = models.CharField(max_length=250,default="")

class linkparser(models.Model):
    keys = models.ForeignKey(keywords,on_delete=models.CASCADE)
    ecom = models.IntegerField(default=0)
    dataparsing = models.DateField(default=now)
    pos = models.IntegerField(default=0)
    region = models.CharField(max_length=250)
    link = models.TextField(default="")
    lower_price = models.CharField(max_length=50,default="")
    old_price = models.CharField(max_length=50,default="")
    brand_name = models.CharField(max_length=250,default="")
    goods_name = models.CharField(max_length=250,default="")



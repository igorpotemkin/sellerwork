from django.utils.timezone import now
from django.db import models


class prod_ozon(models.Model):
    product_id = models.CharField(max_length=100)
    offer_id = models.CharField(max_length=100)
    name = models.CharField(max_length=250, default="")
    barcode = models.CharField(max_length=300, default="")
    sku = models.CharField(max_length=100, default="")#для связки с 1с по артикул
    org = models.IntegerField(default=0)

class metrics_ozon(models.Model):
    product = models.ForeignKey(prod_ozon, on_delete=models.CASCADE)
    org = models.IntegerField(default=0)
    dataparsing = models.DateField(default=now)
    hits_view = models.IntegerField(default=0)
    hits_tocart = models.IntegerField(default=0)
    revenue = models.IntegerField(default=0)
    returns = models.IntegerField(default=0)
    ordered_units = models.IntegerField(default=0)
    cancellations = models.IntegerField(default=0)
    conv_tocart = models.IntegerField(default=0)

class ozon_stocks(models.Model):
    product = models.ForeignKey(prod_ozon, on_delete=models.CASCADE)
    dataparsing = models.DateField(default=now)
    type = models.CharField(max_length=50)
    present = models.IntegerField(default=0)
    reserved = models.IntegerField(default=0)

class ozon_price(models.Model):
    product = models.ForeignKey(prod_ozon, on_delete=models.CASCADE)
    dataparsing = models.DateField(default=now)
    price = models.IntegerField(default=0)
    old_price = models.IntegerField(default=0)
    vat = models.IntegerField(default=0)

class ozon_stock_warehouse(models.Model):
    dataparsing = models.DateField(default=now)
    sku = models.CharField(max_length=100, default="")
    title = models.CharField(max_length=250, default="")
    brand = models.CharField(max_length=200, default="")
    present = models.CharField(max_length=50, default="")
    warehouse = models.CharField(max_length=250, default="")


# Create your models here.

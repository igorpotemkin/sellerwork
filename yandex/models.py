from django.db import models
from django.utils.timezone import now
from api import models as api_models

class sales(models.Model):
    data_sale = models.DateField(default=now)
    idBrand = models.CharField(max_length=50,default="")
    brand = models.CharField(max_length=200,default="")
    sku = models.CharField(max_length=100, default="")#для связки с 1с по артикул
    title = models.CharField(max_length=250)
    hits_view = models.IntegerField(default=0)
    hits_tocart = models.IntegerField(default=0)
    ordered_units = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    revenue = models.IntegerField(default=0)

class stocks(models.Model):
    dataparsing = models.DateField(default=now)
    sku = models.CharField(max_length=100, default="")
    title = models.CharField(max_length=250, default="")
    units = models.IntegerField(default=0)
    warehouse = models.CharField(max_length=250)

class adwords(models.Model):
    keys = models.ForeignKey(api_models.keywords, on_delete=models.CASCADE)
    dataparsing = models.DateField(default=now)
    description = models.CharField(max_length=250, default="")
    quaniti = models.IntegerField(default=0)

class rec_adwords(models.Model):
    keys = models.ForeignKey(api_models.keywords, on_delete=models.CASCADE)
    dataparsing = models.DateField(default=now)
    description = models.CharField(max_length=250, default="")
    quaniti = models.IntegerField(default=0)

class metrics_site(models.Model):
    dataparsing = models.DateField(default=now)
    regionCountry = models.CharField(max_length=250, default="")
    regionArea = models.CharField(max_length=250, default="")
    visits= models.IntegerField(default=0)
    users= models.IntegerField(default=0)
    pageviews= models.IntegerField(default=0)
# Create your models here.

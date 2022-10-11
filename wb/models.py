from django.db import models
from django.utils.timezone import now

class wb_info(models.Model):
    nmId = models.IntegerField(unique=True)
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    promocode = models.IntegerField(default=0)
    org = models.IntegerField(default=0)
    dataparsing = models.DateField(default=now)
# Create your models here.
class wb_products_info(models.Model):
    info = models.ForeignKey(wb_info,on_delete=models.CASCADE)
    object = models.CharField(max_length=200,default="")
    brand = models.CharField(max_length=200,default="")
    vendorCode = models.CharField(max_length=200,default="")
    barcode = models.CharField(max_length=200,default="")

class reports(models.Model):
    nm_id = models.ForeignKey(wb_info, on_delete=models.CASCADE)
    office_name = models.CharField(max_length=200,default="")
    quantity = models.IntegerField(default=0)#Количество
    retail_price = models.DecimalField(max_digits=10,decimal_places=2,default='0.00')#Цена розничная
    retail_amount = models.DecimalField(max_digits=10,decimal_places=2,default='0.00')#Сумма продаж(Возвратов)
    barcode = models.CharField(max_length=200, default="")
    sale_dt = models.DateField(default=now)
    subject_name = models.CharField(max_length=200,default="")#Предмет
    brand_name = models.CharField(max_length=200,default="")#Бренд
    org = models.IntegerField(default=0)

class stock(models.Model):
    barcode = models.CharField(max_length=200, default="")
    quantity = models.IntegerField(default=0)
    warehouse = models.IntegerField(default=0)
    warehouseName = models.CharField(max_length=200, default="")
    nmId = models.CharField(max_length=200, default="")
    subject = models.CharField(max_length=200, default="")
    brand = models.CharField(max_length=200, default="")
    subject = models.CharField(max_length=200, default="")
    Price = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    Discount = models.IntegerField(default=0)
    dataparsing = models.DateField(default=now)

class sales(models.Model):
    saleID = models.CharField(max_length=15, default="")
    date = models.DateField(default=now)
    lastChangeDate = models.DateField(default=now)
    supplierArticle = models.CharField(max_length=200, default="")
    barcode = models.CharField(max_length=200, default="")
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    discountPercent = models.IntegerField(default=0)
    warehouseName = models.CharField(max_length=200, default="")
    forPay = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    finishedPrice = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    priceWithDisc = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    nmId = models.IntegerField(default=0)

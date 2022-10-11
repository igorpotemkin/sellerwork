from django.db import models
from django.utils.timezone import now


class sales_sait(models.Model):
    name = models.CharField(default="", max_length=250)
    xml_id = models.CharField(default="", max_length=36)
    quantity = models.IntegerField()
    order_id = models.IntegerField()
    order_date = models.DateField(default=now)
    is_one_click = models.BooleanField(default=False)
    summ = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')

# Create your models here.

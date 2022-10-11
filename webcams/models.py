from django.db import models

class foto_order(models.Model):
    order = models.CharField(max_length=50,default="")
    link = models.CharField(max_length=500,default="")
# Create your models here.

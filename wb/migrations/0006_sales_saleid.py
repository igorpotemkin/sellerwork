# Generated by Django 4.0.6 on 2022-08-29 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wb', '0005_sales'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='saleID',
            field=models.CharField(default='', max_length=15),
        ),
    ]
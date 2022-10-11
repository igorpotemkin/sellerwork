# Generated by Django 4.0.6 on 2022-08-16 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='prod_ozon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=100)),
                ('offer_id', models.CharField(max_length=100)),
                ('name', models.CharField(default='', max_length=250)),
                ('barcode', models.CharField(default='', max_length=300)),
                ('sku', models.CharField(default='', max_length=100)),
                ('org', models.IntegerField(default=0)),
            ],
        ),
    ]
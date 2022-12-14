# Generated by Django 4.0.6 on 2022-08-30 09:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('yandex', '0002_alter_sales_revenue'),
    ]

    operations = [
        migrations.CreateModel(
            name='stocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataparsing', models.DateField(default=django.utils.timezone.now)),
                ('sku', models.CharField(default='', max_length=100)),
                ('title', models.CharField(max_length=250)),
                ('units', models.CharField(max_length=250)),
                ('warehouse', models.CharField(max_length=250)),
            ],
        ),
    ]

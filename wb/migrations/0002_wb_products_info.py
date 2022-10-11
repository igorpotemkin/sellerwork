# Generated by Django 4.0.6 on 2022-08-19 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='wb_products_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object', models.CharField(default='', max_length=200)),
                ('brand', models.CharField(default='', max_length=200)),
                ('vendorCode', models.CharField(default='', max_length=200)),
                ('barcode', models.CharField(default='', max_length=200)),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wb.wb_info')),
            ],
        ),
    ]

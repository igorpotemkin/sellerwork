# Generated by Django 4.0.6 on 2022-08-17 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ozon', '0002_metrics_ozon'),
    ]

    operations = [
        migrations.AddField(
            model_name='metrics_ozon',
            name='cancellations',
            field=models.IntegerField(default=0),
        ),
    ]
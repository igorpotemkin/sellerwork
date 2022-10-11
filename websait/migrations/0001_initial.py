# Generated by Django 4.0.6 on 2022-09-22 06:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sales_sait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=250)),
                ('xml_id', models.CharField(default='', max_length=36)),
                ('quantity', models.IntegerField()),
                ('order_id', models.IntegerField()),
                ('order_date', models.DateField(default=django.utils.timezone.now)),
                ('is_one_click', models.BooleanField(default=False)),
                ('summ', models.DecimalField(decimal_places=2, default='0.00', max_digits=10)),
            ],
        ),
    ]

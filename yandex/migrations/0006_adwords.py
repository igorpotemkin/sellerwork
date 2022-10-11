# Generated by Django 4.0.6 on 2022-09-16 12:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_keywords_linkparser'),
        ('yandex', '0005_alter_stocks_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='adwords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataparsing', models.DateField(default=django.utils.timezone.now)),
                ('description', models.CharField(default='', max_length=250)),
                ('quaniti', models.IntegerField(default=0)),
                ('keys', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.keywords')),
            ],
        ),
    ]

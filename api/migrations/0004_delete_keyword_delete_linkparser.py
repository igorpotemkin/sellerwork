# Generated by Django 4.0.6 on 2022-09-07 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_keyword'),
    ]

    operations = [
        migrations.DeleteModel(
            name='keyword',
        ),
        migrations.DeleteModel(
            name='linkparser',
        ),
    ]

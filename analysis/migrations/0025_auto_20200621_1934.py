# Generated by Django 3.0.7 on 2020-06-21 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0024_auto_20200621_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysis',
            name='tweets',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='analysis',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 21, 19, 34, 45, 603312)),
        ),
    ]

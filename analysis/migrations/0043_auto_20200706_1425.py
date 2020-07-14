# Generated by Django 3.0.8 on 2020-07-06 08:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0042_auto_20200706_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysis',
            name='trending_keywords',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='analysis',
            name='trending_tweets',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 14, 25, 5, 688575)),
        ),
    ]

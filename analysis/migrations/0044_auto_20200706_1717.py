# Generated by Django 3.0.8 on 2020-07-06 11:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0043_auto_20200706_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 17, 17, 46, 509447)),
        ),
    ]

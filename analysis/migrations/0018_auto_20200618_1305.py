# Generated by Django 3.0.7 on 2020-06-18 07:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0017_auto_20200618_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 18, 13, 5, 22, 714623)),
        ),
    ]

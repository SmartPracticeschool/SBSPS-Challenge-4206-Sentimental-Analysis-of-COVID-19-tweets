# Generated by Django 3.0.7 on 2020-06-21 04:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0020_auto_20200621_0951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='constants',
            old_name='number_of_tweets',
            new_name='number_of_tweets_to_fetch_for_analysis',
        ),
        migrations.AlterField(
            model_name='analysis',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 21, 9, 53, 18, 122984)),
        ),
    ]

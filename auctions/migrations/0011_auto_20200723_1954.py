# Generated by Django 3.0.8 on 2020-07-23 14:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20200723_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activelistings',
            name='created_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 23, 14, 9, 50, 484224, tzinfo=utc)),
        ),
    ]

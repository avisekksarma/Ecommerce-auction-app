# Generated by Django 3.0.8 on 2020-07-26 14:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auto_20200726_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='status',
            field=models.CharField(default='active', max_length=10),
        ),
        migrations.AlterField(
            model_name='listings',
            name='created_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 26, 14, 4, 16, 681740, tzinfo=utc)),
        ),
    ]

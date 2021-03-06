# Generated by Django 3.0.8 on 2020-07-23 14:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20200723_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='activelistings',
            name='highest_bidder',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='highest_bidder', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activelistings',
            name='number_of_bids',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='activelistings',
            name='created_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 23, 14, 38, 59, 168797, tzinfo=utc)),
        ),
    ]

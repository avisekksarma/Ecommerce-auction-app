# Generated by Django 3.1 on 2020-08-15 14:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_auto_20200815_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='category',
            field=models.CharField(blank=True, choices=[('FASHION', 'FASHION'), ('HOME', 'HOME'), ('ELECTRONICS', 'ELECTRONICS'), ('SPORTS', 'SPORTS'), ('HEALTH AND BEAUTY', 'HEALTH AND BEAUTY'), ('TOYS OR BABY ITEMS', 'TOYS OR BABY ITEMS'), ('VEHICLE PARTS AND MOTORS', 'VEHICLE PARTS AND MOTORS'), ('OTHERS', 'OTHERS')], default='OTHERS', max_length=30),
        ),
        migrations.AlterField(
            model_name='listings',
            name='created_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 15, 14, 39, 40, 928883, tzinfo=utc)),
        ),
    ]
# Generated by Django 3.1 on 2020-08-15 14:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_auto_20200726_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='category',
            field=models.CharField(choices=[('FASHION', 'FASHION'), ('HOME', 'HOME'), ('ELECTRONICS', 'ELECTRONICS'), ('SPORTS', 'SPORTS'), ('HEALTH AND BEAUTY', 'HEALTH AND BEAUTY'), ('TOYS OR BABY ITEMS', 'TOYS OR BABY ITEMS'), ('VEHICLE PARTS AND MOTORS', 'VEHICLE PARTS AND MOTORS'), ('OTHERS', 'OTHERS')], default='OTHERS', max_length=30),
        ),
        migrations.AlterField(
            model_name='listings',
            name='created_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 15, 14, 33, 1, 338962, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='listings',
            name='image',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]

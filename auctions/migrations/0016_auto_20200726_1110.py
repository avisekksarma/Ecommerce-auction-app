# Generated by Django 3.0.8 on 2020-07-26 05:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('auctions', '0015_auto_20200726_0929'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ActiveListings',
            new_name='Listings'
        ),
        migrations.AlterField(
            model_name='bid',
            name='listing',
            field=models.IntegerField()
        ),
        migrations.AlterField(
            model_name='comment',
            name='listing',
            field=models.IntegerField()
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='listing',
            field=models.IntegerField()
        ),

    ]
# Generated by Django 3.0.8 on 2020-07-26 14:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('auctions', '0017_auto_20200726_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='listing',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bid',
                                       to='auctions.Listings'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment',
                                    to='auctions.Listings'),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlists',
                                    to='auctions.Listings'),
        ),

    ]

# Generated by Django 3.0.8 on 2020-07-24 02:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_auto_20200723_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activelistings',
            name='current_bid',
        ),
        migrations.RemoveField(
            model_name='activelistings',
            name='highest_bidder',
        ),
        migrations.RemoveField(
            model_name='activelistings',
            name='number_of_bids',
        ),
        migrations.AlterField(
            model_name='activelistings',
            name='created_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 24, 2, 19, 4, 676932, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to=settings.AUTH_USER_MODEL)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='auctions.ActiveListings')),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_bids', models.IntegerField(default=0)),
                ('current_bid', models.FloatField()),
                ('highest_bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='highest_bidder', to=settings.AUTH_USER_MODEL)),
                ('listing', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bid', to='auctions.ActiveListings')),
            ],
        ),
    ]
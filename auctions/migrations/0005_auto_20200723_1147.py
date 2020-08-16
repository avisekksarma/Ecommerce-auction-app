# Generated by Django 3.0.8 on 2020-07-23 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20200723_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activelistings',
            name='price',
        ),
        migrations.AddField(
            model_name='activelistings',
            name='initial_bid',
            field=models.FloatField(default=0, verbose_name='Initial Bid'),
        ),
        migrations.AlterField(
            model_name='activelistings',
            name='title',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]

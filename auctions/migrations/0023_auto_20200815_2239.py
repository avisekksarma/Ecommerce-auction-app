# Generated by Django 3.1 on 2020-08-15 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0022_auto_20200815_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='listings',
            name='created_datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

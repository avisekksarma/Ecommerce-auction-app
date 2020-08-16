# Generated by Django 3.0.8 on 2020-07-23 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveListings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(max_length=200, upload_to='auctions/static/auctions/image')),
            ],
        ),
    ]

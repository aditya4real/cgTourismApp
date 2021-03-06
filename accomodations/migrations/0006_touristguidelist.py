# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-15 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accomodations', '0005_citywisehotellist'),
    ]

    operations = [
        migrations.CreateModel(
            name='TouristGuideList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.CharField(blank=True, max_length=15)),
                ('district', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Tourist Guide List',
            },
        ),
    ]

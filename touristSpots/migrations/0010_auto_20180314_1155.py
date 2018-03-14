# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-14 06:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('touristSpots', '0009_auto_20180314_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='place',
        ),
        migrations.AddField(
            model_name='places',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='touristSpots.Category'),
        ),
    ]
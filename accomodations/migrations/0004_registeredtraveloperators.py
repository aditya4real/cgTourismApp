# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-15 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accomodations', '0003_registeredhotels'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredTravelOperators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=255)),
                ('contact_no', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Registered Tour and Travel Operators',
            },
        ),
    ]

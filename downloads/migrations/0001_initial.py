# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-16 10:36
from __future__ import unicode_literals

from django.db import migrations, models
import downloads.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brochure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('pdf', models.FileField(upload_to=downloads.models.get_upload_url)),
            ],
            options={
                'verbose_name_plural': 'Brochures',
            },
        ),
    ]

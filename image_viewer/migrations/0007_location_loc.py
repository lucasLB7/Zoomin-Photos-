# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-09 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_viewer', '0006_location_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='loc',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
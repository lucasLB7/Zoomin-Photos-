# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-09 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_viewer', '0003_auto_20180609_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('continent', models.CharField(choices=[('AFRICA', 'Africa'), ('EUROPE', 'Europe'), ('ASIA', 'Asia'), ('NORTH AMERICA', 'N_America'), ('SOUTH AMERICA', 'S_America'), ('AUSTRALIA', 'Australia'), ('ANTARCTICA', 'Antarctica')], default='AFRICA', max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Location',
            },
        ),
        migrations.RemoveField(
            model_name='image',
            name='location',
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ManyToManyField(related_name='location', to='image_viewer.Location'),
        ),
    ]
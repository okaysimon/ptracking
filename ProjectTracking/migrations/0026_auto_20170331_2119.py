# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectTracking', '0025_auto_20170331_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='r_info_value',
            field=models.CharField(default='无', max_length=500, verbose_name='价值'),
        ),
    ]

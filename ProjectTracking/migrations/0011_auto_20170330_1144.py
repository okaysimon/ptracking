# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-30 03:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectTracking', '0010_auto_20170330_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='r_workload',
            field=models.FloatField(default=None, null=True, verbose_name='工作量'),
        ),
    ]
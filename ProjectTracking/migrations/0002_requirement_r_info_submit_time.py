# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 15:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectTracking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='r_info_submit_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

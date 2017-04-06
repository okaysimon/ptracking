# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 16:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectTracking', '0028_auto_20170407_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='r_info_submit_employee',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ProjectTracking.Employee', verbose_name='submit employee'),
            preserve_default=False,
        ),
    ]

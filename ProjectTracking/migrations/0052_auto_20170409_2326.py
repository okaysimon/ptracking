# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-09 15:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectTracking', '0051_auto_20170409_2324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requirement',
            old_name='r_info_submit_user',
            new_name='i_submit_user',
        ),
        migrations.RenameField(
            model_name='requirement',
            old_name='r_info_value',
            new_name='i_value',
        ),
    ]

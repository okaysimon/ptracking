# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-09 15:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectTracking', '0049_auto_20170409_2322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requirement',
            old_name='r_info_name',
            new_name='i_name',
        ),
    ]

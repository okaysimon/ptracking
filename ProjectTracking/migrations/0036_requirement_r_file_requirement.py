# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectTracking', '0035_auto_20170408_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='r_file_requirement',
            field=models.FileField(null=True, upload_to='uploads/', verbose_name='需求文档'),
        ),
    ]

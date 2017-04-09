# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-09 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectTracking', '0046_remove_requirement_r_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='r_category',
            field=models.CharField(blank=True, choices=[('0', '开发类'), ('1', '运维类'), ('2', '紧急类')], default='', max_length=1, null=True, verbose_name='需求类别'),
        ),
    ]

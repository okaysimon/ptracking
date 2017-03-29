# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('r_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('r_info_name', models.CharField(default='', max_length=100, verbose_name='需求名称')),
                ('r_info_submit_person', models.CharField(default='', max_length=10, verbose_name='提出人')),
                ('r_info_value', models.CharField(default='', max_length=500, verbose_name='价值')),
                ('r_leader', models.CharField(default='', max_length=20)),
                ('r_value_ok', models.BooleanField(default=False)),
                ('r_handle', models.CharField(default='', max_length=50)),
                ('r_status', models.CharField(default='', max_length=50)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectTracking', '0006_auto_20170330_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='r_category',
            field=models.CharField(blank=True, choices=[('0', '开发类'), ('1', '运维类'), ('2', '紧急类')], default='', max_length=10, verbose_name='需求类别'),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='r_info_submit_department',
            field=models.CharField(choices=[('0', '总裁室'), ('1', '综合部'), ('2', '财务部'), ('3', '创新业务部'), ('4', '网络销售部'), ('5', '产险销售部'), ('6', '寿险电销部'), ('7', '数据管理部'), ('8', '信息技术部')], default='0', max_length=10, verbose_name='提出部门'),
        ),
    ]
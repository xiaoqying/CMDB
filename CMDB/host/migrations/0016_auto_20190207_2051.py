# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-07 12:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0015_auto_20190130_1610'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': '一级菜单'},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'verbose_name': '岗位'},
        ),
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': '用户信息'},
        ),
    ]

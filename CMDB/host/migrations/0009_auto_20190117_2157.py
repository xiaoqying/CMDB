# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-17 13:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0008_auto_20190117_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostlist',
            name='host_region_computer_room_id',
        ),
        migrations.RemoveField(
            model_name='region',
            name='computer_room',
        ),
        migrations.AddField(
            model_name='hostlist',
            name='computer_room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='host.ComputerRoom', verbose_name='机房'),
        ),
    ]

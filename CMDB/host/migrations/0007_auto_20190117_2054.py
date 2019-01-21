# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-17 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0006_auto_20190117_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='computer_room',
        ),
        migrations.AddField(
            model_name='region',
            name='computer_room',
            field=models.ManyToManyField(null=True, to='host.ComputerRoom', verbose_name='机房'),
        ),
    ]
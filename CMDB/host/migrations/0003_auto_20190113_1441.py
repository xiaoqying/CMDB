# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-13 06:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0002_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, null=True, verbose_name='机房')),
            ],
            options={
                'verbose_name_plural': '机房表',
            },
        ),
        migrations.AddField(
            model_name='hostlist',
            name='cpu',
            field=models.CharField(max_length=32, null=True, verbose_name='CPU'),
        ),
        migrations.AddField(
            model_name='hostlist',
            name='disk',
            field=models.CharField(max_length=32, null=True, verbose_name='磁盘'),
        ),
        migrations.AddField(
            model_name='hostlist',
            name='mem',
            field=models.CharField(max_length=32, null=True, verbose_name='内存'),
        ),
        migrations.AlterField(
            model_name='hostlist',
            name='hostname',
            field=models.CharField(max_length=32, null=True, verbose_name='主机名'),
        ),
        migrations.AlterField(
            model_name='hostlist',
            name='ipaddress',
            field=models.CharField(max_length=32, null=True, verbose_name='IP地址'),
        ),
        migrations.AlterField(
            model_name='hostlist',
            name='system',
            field=models.CharField(max_length=32, null=True, verbose_name='操作系统'),
        ),
        migrations.AddField(
            model_name='hostlist',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='host.Region', verbose_name='机房'),
        ),
    ]

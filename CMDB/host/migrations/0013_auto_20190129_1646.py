# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-29 08:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0012_auto_20190117_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('icon', models.CharField(blank=True, max_length=64, null=True, verbose_name='图标')),
                ('weight', models.IntegerField(default=1, verbose_name='显示权重')),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=32, verbose_name='权限')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('name', models.CharField(max_length=32, verbose_name='URL别名')),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='host.Menu')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='host.Permission')),
            ],
            options={
                'verbose_name': '权限',
                'verbose_name_plural': '权限',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
                ('permissions', models.ManyToManyField(blank=True, to='host.Permission', verbose_name='角色拥有的权限')),
            ],
        ),
        migrations.AlterField(
            model_name='computerroom',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='机房'),
        ),
        migrations.AlterField(
            model_name='hostlist',
            name='cpu',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='CPU'),
        ),
        migrations.AlterField(
            model_name='hostlist',
            name='disk',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='磁盘'),
        ),
        migrations.AlterField(
            model_name='hostlist',
            name='hostname',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='主机名'),
        ),
        migrations.AlterField(
            model_name='hostlist',
            name='ipaddress',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='IP地址'),
        ),
        migrations.AlterField(
            model_name='hostlist',
            name='mem',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='内存'),
        ),
        migrations.AlterField(
            model_name='hostlist',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='host.Region', verbose_name='区域'),
        ),
        migrations.AlterField(
            model_name='hostlist',
            name='system',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='操作系统'),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='区域'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='用户名'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='roles',
            field=models.ManyToManyField(blank=True, to='host.Role', verbose_name='用户拥有的角色'),
        ),
    ]
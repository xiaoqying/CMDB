# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-17 12:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0005_auto_20190116_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, null=True, verbose_name='机房')),
            ],
            options={
                'verbose_name_plural': '机房表',
            },
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name_plural': '区域表'},
        ),
        migrations.AlterField(
            model_name='hostlist',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='host.Region', verbose_name='区域'),
        ),
        migrations.AddField(
            model_name='region',
            name='computer_room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='host.ComputerRoom', verbose_name='机房'),
        ),
    ]
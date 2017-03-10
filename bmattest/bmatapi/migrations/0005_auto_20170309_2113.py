# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmatapi', '0004_auto_20170309_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='id',
        ),
        migrations.RemoveField(
            model_name='performer',
            name='id',
        ),
        migrations.AlterField(
            model_name='channel',
            name='name',
            field=models.CharField(max_length=150, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='performer',
            name='name',
            field=models.CharField(max_length=150, primary_key=True, serialize=False),
        ),
    ]

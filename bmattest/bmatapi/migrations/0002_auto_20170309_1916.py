# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmatapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]

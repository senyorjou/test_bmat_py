# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmatapi', '0005_auto_20170309_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='length',
            field=models.IntegerField(default=0),
        ),
    ]

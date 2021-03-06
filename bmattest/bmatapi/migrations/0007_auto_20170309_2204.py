# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 22:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bmatapi', '0006_auto_20170309_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bmatapi.Channel')),
                ('performer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bmatapi.Performer')),
            ],
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='play',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bmatapi.Song', to_field='title'),
        ),
    ]

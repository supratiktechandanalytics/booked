# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-14 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_auto_20170514_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.IntegerField(),
        ),
    ]

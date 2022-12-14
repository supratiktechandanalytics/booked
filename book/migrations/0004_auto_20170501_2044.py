# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-01 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20170501_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='position',
            field=models.CharField(default=10, max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='seat',
            name='status',
            field=models.CharField(choices=[('available', 'available'), ('reserved', 'reserved'), ('unavailable', 'unavailable')], default='Available', max_length=20),
        ),
    ]
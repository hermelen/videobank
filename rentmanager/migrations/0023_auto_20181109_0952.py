# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-09 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentmanager', '0022_merge_20181108_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movierent',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

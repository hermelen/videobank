# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-06 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentmanager', '0012_auto_20181106_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, to='rentmanager.Actor'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-11 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentmanager', '0024_auto_20181111_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Pr\xe9nom'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Nom'),
        ),
    ]
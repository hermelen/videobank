# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-06 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentmanager', '0020_auto_20181106_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Titre'),
        ),
    ]
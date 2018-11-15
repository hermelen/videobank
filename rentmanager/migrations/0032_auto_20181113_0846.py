# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-13 08:46
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentmanager', '0031_auto_20181112_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movietranslation',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, blank=True, editable=False, null=True, populate_from='title', unique=True, verbose_name='slug'),
        ),
    ]
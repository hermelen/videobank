# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-06 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentmanager', '0014_actor_movies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='movies',
            field=models.ManyToManyField(blank=True, to='rentmanager.Movie'),
        ),
    ]
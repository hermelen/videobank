# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-12 13:38
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentmanager', '0027_auto_20181112_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('synopsis', models.TextField(blank=True, null=True, verbose_name='synopsis')),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='title', unique=True, verbose_name='slug')),
            ],
            options={
                'managed': True,
                'db_table': 'rentmanager_movie_translation',
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'movie Translation',
            },
        ),
        migrations.RemoveField(
            model_name='movie',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='synopsis',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='title',
        ),
        migrations.AddField(
            model_name='movietranslation',
            name='master',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='rentmanager.Movie'),
        ),
        migrations.AlterUniqueTogether(
            name='movietranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-05 12:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentmanager', '0007_auto_20181105_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Pays')),
            ],
        ),
        migrations.AlterField(
            model_name='director',
            name='picture',
            field=models.ImageField(null=True, upload_to='directors', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rentmanager.Country'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-05 09:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields
import userena.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mugshot', easy_thumbnails.fields.ThumbnailerImageField(blank=True, help_text='A personal image displayed in your profile.', upload_to=userena.models.upload_to_mugshot, verbose_name='mugshot')),
                ('privacy', models.CharField(choices=[(b'open', 'Open'), (b'registered', 'Registered'), (b'closed', 'Closed')], default=b'registered', help_text='Designates who can view your profile.', max_length=15, verbose_name='privacy')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='my_profile', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'default_permissions': ('add', 'change', 'delete'),
                'abstract': False,
                'permissions': (('view_profile', 'Can view profile'),),
            },
        ),
    ]

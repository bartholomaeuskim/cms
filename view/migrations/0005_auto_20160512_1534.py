# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-12 06:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('view', '0004_auto_20160512_1532'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Codes',
            new_name='Code',
        ),
        migrations.RenameModel(
            old_name='Colors',
            new_name='Color',
        ),
        migrations.RenameModel(
            old_name='Vehicles',
            new_name='Vehicle',
        ),
    ]

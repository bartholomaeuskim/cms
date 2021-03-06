# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-12 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=16)),
                ('brand', models.CharField(max_length=10)),
                ('model', models.CharField(max_length=255)),
                ('trim', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255)),
                ('color_code', models.CharField(max_length=4)),
                ('color', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='vehilces',
            old_name='colorcode',
            new_name='color_code',
        ),
    ]

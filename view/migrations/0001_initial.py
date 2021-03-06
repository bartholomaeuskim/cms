# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-12 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehilces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(max_length=17)),
                ('code', models.CharField(max_length=16)),
                ('colorcode', models.CharField(max_length=4)),
                ('option', models.CharField(max_length=255)),
                ('seats', models.CharField(max_length=4)),
                ('cif', models.IntegerField()),
                ('produced_month', models.CharField(max_length=6)),
                ('departure_date', models.DateField()),
                ('arrival_date', models.DateField()),
                ('kaida_reg_date', models.DateField()),
                ('sagai_reg_date', models.DateField()),
            ],
        ),
    ]

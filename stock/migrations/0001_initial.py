# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-15 00:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('item_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('available_qty', models.FloatField(blank=True, null=True)),
                ('reserved_qty', models.FloatField(blank=True, null=True)),
                ('ordered_qty', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]

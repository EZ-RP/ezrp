# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-07 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_number', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('item_desc', models.CharField(max_length=120, verbose_name='Description')),
                ('unit', models.CharField(max_length=10)),
                ('product_category', models.CharField(max_length=30)),
                ('fulfilment_type', models.CharField(choices=[('P', 'Purchase'), ('M', 'Production')], max_length=1)),
            ],
            options={
                'db_table': 'product_item',
                'managed': True,
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 08:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemId', models.CharField(max_length=30)),
                ('itemDescription', models.CharField(max_length=120)),
                ('units', models.CharField(max_length=30)),
                ('productCategory', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Item_Attributes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
                ('thickness', models.IntegerField()),
                ('grade', models.CharField(max_length=30)),
                ('weight', models.IntegerField()),
                ('itemId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Item')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-15 00:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=8)),
                ('product_category', models.CharField(blank=True, max_length=30, null=True)),
                ('item_id', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField()),
                ('account_number', models.CharField(max_length=8)),
                ('order_type', models.CharField(choices=[('S', 'Sale'), ('P', 'Purchase')], max_length=1)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('delivery_date', models.DateField()),
                ('order_status', models.CharField(choices=[('C', 'Created'), ('O', 'Ordered'), ('D', 'Delivered'), ('I', 'Invoiced')], max_length=1)),
                ('invoice_date', models.DateTimeField(blank=True, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Address')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_line_id', models.IntegerField()),
                ('item_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('discount_price', models.FloatField()),
                ('unit', models.CharField(max_length=10)),
                ('order_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
            ],
        ),
    ]

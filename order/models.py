from django.db import models
from base.models import Address
from party.models import Party
from product.models import Item


"""Naming conventions:
    - Class names                           = CamelCase
    - Function or model field names         = lowercase_underscore"""


class Order(models.Model):
    ORDER_STATUS = (
        ('C', 'Created'),
        ('O', 'Ordered'),
        ('D', 'Delivered'),
        ('I', 'Invoiced')
    )
    ORDER_TYPE = (
        ('S', 'Sale'),
        ('P', 'Purchase')
    )
    order_number = models.IntegerField()
    account_number = models.ForeignKey(Party)  # models.CharField(max_length=8)
    order_type = models.CharField(max_length=1, choices=ORDER_TYPE)
    address = models.ForeignKey(Address)
    created_date = models.DateTimeField(auto_now=True)
    delivery_date = models.DateField()
    order_status = models.CharField(max_length=1, choices=ORDER_STATUS)
    invoice_date = models.DateTimeField(null=True, blank=True)


class OrderLine(models.Model):
    order_line_id = models.IntegerField()
    order_number = models.ForeignKey(Order)
    item_id = models.ForeignKey(Item) #models.IntegerField()
    quantity = models.IntegerField()
    price = models.FloatField()
    discount_price = models.FloatField()
    unit = models.CharField(max_length=10)


class Discounts(models.Model):
    account_number = models.CharField(max_length=8)
    product_category = models.CharField(max_length=30, null=True, blank=True)
    item_id = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)




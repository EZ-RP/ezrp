from django.db import models
from base.models import Address
from django.contrib.admin import widgets


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
    account_number = models.CharField(max_length=8)
    order_type = models.CharField(max_length=1, choices=ORDER_TYPE)
    address = models.ForeignKey(Address)
    created_date = models.DateTimeField(auto_now=True)
    delivery_date = models.DateField()
    order_status = models.CharField(max_length=1, choices=ORDER_STATUS)
    invoice_date = models.DateTimeField(null=True, blank=True)


class OrderLine(models.Model):
    order_line_id = models.IntegerField()
    order_number = models.ForeignKey(Order)
    item_id = models.IntegerField()
    quantity = models.IntegerField()
    price = models.FloatField()
    discount_price = models.FloatField()
    unit = models.CharField(max_length=10)


# DS: Base Attribute Value Table -- removed until post release upgrade
class ProductAttributeDimensions(models.Model):
    PRODUCT_DIMS = (
        ('Dim1', 'Dimension 1'),
        ('Dim2', 'Dimension 2'),
        ('Dim3', 'Dimension 3'),
        ('Dim4', 'Dimension 4'),
        ('Dim5', 'Dimension 5'),
        ('Dim6', 'Dimension 6'),
        ('Dim7', 'Dimension 7'),
        ('Dim8', 'Dimension 8')
    )
    product_category = models.CharField(max_length=30)
    dim = models.CharField(max_length=1, choices=PRODUCT_DIMS)
    required = models.BooleanField()


# DS: Base Attribute Value Table -- removed until post release upgrade
class DiscountAttributeTypes(models.Model):
    product_category = models.CharField(max_length=30)
    dimension_1 = models.CharField(max_length=50, null=True, blank=True)
    dimension_2 = models.CharField(max_length=50, null=True, blank=True)
    dimension_3 = models.CharField(max_length=50, null=True, blank=True)
    dimension_4 = models.CharField(max_length=50, null=True, blank=True)
    dimension_5 = models.CharField(max_length=50, null=True, blank=True)
    dimension_6 = models.CharField(max_length=50, null=True, blank=True)
    dimension_7 = models.CharField(max_length=50, null=True, blank=True)
    dimension_8 = models.CharField(max_length=50, null=True, blank=True)


# DS: Base Attribute Value Table -- removed until post release upgrade
class DiscountAttributeValues(models.Model):
    APPLY_TYPE = (
        ('Add', 'Add to price'),
        ('Apply', 'Apply to price')
    )
    product_attribute_type = models.ForeignKey(DiscountAttributeTypes)
    value = models.FloatField()
    apply_type = models.CharField(max_length=1, choices=APPLY_TYPE)


from django.db import models
from base import models


# Create your models here.
class Order(models.Model):
    ORDER_STATUS = (
        ('Created', 'Created')
        ('Confirmed', 'Confirmed')
        ('Delivered', 'Delivered')
        ('Invoiced', 'Invoiced')
    )
    ORDER_TYPE = (
        ('S', 'Sale'),
        ('P', 'Purchase')
    )
    OrderNumber = models.IntegerField()
    AccountNumber = models.CharField(max_length=8)
    OrderType = models.CharField(max_length=1, choices=ORDER_TYPE)
    Address = models.ForeignKey(models.Address)
    CreatedDate = models.DateTimeField(auto_now=True)
    DeliveryDate = models.DateTimeField()
    OrderStatus = models.CharField(max_length=1, choices=ORDER_STATUS)
    InvoiceDate = models.DateTimeField()


class OrderLine(models.Model):
    OrderLineId = models.IntegerField()
    OrderNumber = models.ForeignKey(Order)
    ItemId = models.IntegerField()
    Quantity = models.IntegerField()
    Price = models.FloatField()
    DiscountPrice = models.FloatField()
    Unit = models.CharField()


# DS: Base Attribute Value Table
class ProductAttributeDimensions(models.Model):
    PRODUCT_DIMS = (
        ('Dim1', 'Dimension 1')
        ('Dim2', 'Dimension 2')
        ('Dim3', 'Dimension 3')
        ('Dim4', 'Dimension 4')
        ('Dim5', 'Dimension 5')
        ('Dim6', 'Dimension 6')
        ('Dim7', 'Dimension 7')
        ('Dim8', 'Dimension 8')
    )
    productCategory = models.CharField(max_length=30)
    dim = models.CharField(max_length=1, choices=PRODUCT_DIMS)
    required = models.BooleanField()


# DS: Base Attribute Value Table
class DiscountAttributeTypes(models.Model):
    productCategory = models.CharField(max_length=30)
    dimension1 = models.CharField(max_length=50)
    dimension2 = models.CharField(max_length=50)
    dimension3 = models.CharField(max_length=50)
    dimension4 = models.CharField(max_length=50)
    dimension5 = models.CharField(max_length=50)
    dimension6 = models.CharField(max_length=50)
    dimension7 = models.CharField(max_length=50)
    dimension8 = models.CharField(max_length=50)


# DS: Base Attribute Value Table
class DiscountAttributeValues(models.Model):
    APPLY_TYPE = (
        ('Add', 'Add to price')
        ('Apply', 'Apply to price')
    )
    productAttributeType = models.ForeignKey(DiscountAttributeTypes)
    value = models.FloatField()
    applyType = models.CharField()
from django.db import models

# Create your models here.
class Order(models.Model):
    ORDER_TYPE = (
        ('S', 'Sale'),
        ('P', 'Purchase')
    )
    OrderLineId = models.IntegerField()
    OrderNumber = models.IntegerField()
    OrderType = models.CharField(max_length=1, choices=ORDER_TYPE)
    ItemId = models.IntegerField()

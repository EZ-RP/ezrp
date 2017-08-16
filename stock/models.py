from django.db import models
# Create your models here.

class Inventory(models.Model)
    itemID = models.CharField(max_length=30, unique=True)
    availiableQuantity = models.IntegerField
    reservedQuantity = models.IntegerField
    orderedQuantity = models.IntegerField
from django.db import models

# Create your models here.
class Item(models.Model):
    itemId = models.CharField(max_length=30)
    itemDescription = models.CharField(max_length=120)
    units = models.CharField(max_length=30)
    productCategory = models.CharField(max_length=30)

class Item_Attributes(models.Model):
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE)
    height = models.IntegerField()
    width = models.IntegerField()
    thickness = models.IntegerField()
    grade = models.CharField(max_length= 30)
    weight = models.IntegerField()

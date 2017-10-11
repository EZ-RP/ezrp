from django.db import models


"""Naming conventions:
    - Class names                           = CamelCase
    - Function or model field names         = lowercase_underscore"""


class Item(models.Model):
    item_id = models.CharField(max_length=30)
    item_desc = models.CharField(max_length=120)
    units = models.CharField(max_length=30)
    product_category = models.CharField(max_length=30)


# DS: removed until post release upgrade
class ItemAttribute(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    height = models.IntegerField()
    width = models.IntegerField()
    thickness = models.IntegerField()
    grade = models.CharField(max_length= 30)
    weight = models.IntegerField()




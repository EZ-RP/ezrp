from django.db import models


"""Naming conventions:
    - Class names                           = CamelCase
    - Function or model field names         = lowercase_underscore"""

class Inventory(models.Model):
    item_id = models.CharField(max_length=30, primary_key=True)
    available_qty = models.IntegerField
    reserved_qty = models.IntegerField
    ordered_qty = models.IntegerField
from django.db import models


"""Naming conventions:
    - Class names                           = CamelCase
    - Function or model field names         = lowercase_underscore"""


class Inventory(models.Model):
    item_id = models.CharField(max_length=30, primary_key=True)
    available_qty = models.FloatField(null=True, blank=True)
    reserved_qty = models.FloatField(null=True, blank=True)
    ordered_qty = models.FloatField(null=True, blank=True)

    def reserve_qty(self, qty: float):
        if self.available_qty >= qty:
            self.reserved_qty += qty
            self.available_qty -= qty
            self.save()
            return 0
        else:
            return qty - self.available_qty



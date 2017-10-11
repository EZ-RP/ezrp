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
        """
        Call method to reserve a qty of an item.
        Return value is the qty not reserved, if any, else zero
        :param qty:
        :return Qty not reserved:
        """
        if self.available_qty >= qty:
            self.reserved_qty += qty
            self.available_qty -= qty
            self.save()
            return 0
        else:
            return qty - self.available_qty

    def return_reserved_qty(self, qty: float):
        """
        Call method to return reserved qty of an item to available stock.
        Return value is the qty not returned, if any, else zero
        :param qty:
        :return Qty not returned:
        """
        if self.reserved_qty >= qty:
            self.available_qty += qty
            self.reserved_qty -= qty
            self.save()
            return 0
        else:
            return qty - self.reserved_qty

    def quantity_received(self, qty: float):
        """
        Call method to increase available stock from a purchase order.
        """
        self.available_qty += qty
        self.save()
        return 0

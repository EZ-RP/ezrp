from django.db import models
from product.models import *

"""Naming conventions:
    - Class names                           = CamelCase
    - Function or model field names         = lowercase_underscore"""


class Inventory(models.Model):
    item_id = models.ForeignKey(Item)  # models.CharField(max_length=30, primary_key=True)
    available_qty = models.FloatField(null=True, blank=True)
    reserved_qty = models.FloatField(null=True, blank=True)
    ordered_qty = models.FloatField(null=True, blank=True)

    def get_next_id(self):
        last_inv = Inventory.objects.all().order_by('-id').first()
        if last_inv != None:
            return last_inv.id + 1
        else:
            return 1

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

    def remove_reserved_qty(self, qty: float):
        """
        Call method to remove the reserved qty of an item once it is shipped to the customer.
        Return value is the qty not removed, if any, else zero
        :param qty:
        :return Qty not removed:
        """
        if self.reserved_qty >= qty:
            self.reserved_qty -= qty
            self.save()
            return 0
        else:
            return qty - self.reserved_qty

    def add_ordered_qty(self, qty: float):
        """
        Call method to increase ordered stock qty.
        """
        self.ordered_qty += qty
        self.save()
        return 0

    def add_ordered_to_available(self, qty: float):
        """
        Call method to add ordered qty of an item to available stock.
        Return value is the qty not added, if any, else zero
        :param qty:
        :return Qty not added:
        """
        if self.ordered_qty >= qty:
            self.available_qty += qty
            self.ordered_qty -= qty
            self.save()
            return 0
        else:
            return qty - self.ordered_qty

    def add_ordered_to_reserved(self, qty: float):
        """
        Call method to add ordered qty of an item to reserved stock.
        Return value is the qty not added, if any, else zero
        :param qty:
        :return Qty not added:
        """
        if self.ordered_qty >= qty:
            self.reserved_qty += qty
            self.ordered_qty -= qty
            self.save()
            return 0
        else:
            return qty - self.ordered_qty


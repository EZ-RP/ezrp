from django.db import models
from base.models import Address
from party.models import Party
from product.models import Item


"""Naming conventions:
    - Class names                           = CamelCase
    - Function or model field names         = lowercase_underscore"""


class Order(models.Model):
    """
    Stores an Order Record including relevant customer information and dates,
    related to :model:`party.Party` and :model:`base.Address`.
    """
    ORDER_STATUS = (
        ('C', 'Created'),
        ('O', 'Ordered'),
        ('D', 'Delivered'),
        ('I', 'Invoiced')
    )
    ORDER_TYPE = (
        ('S', 'Sale'),
        ('P', 'Purchase'),
        ('M', 'Production')
    )
    order_number = models.IntegerField(help_text="Order Identifier (unique)")
    account_number = models.ForeignKey(Party, help_text="Link to the Account related to this order")
    order_type = models.CharField(max_length=1, choices=ORDER_TYPE, help_text="Type of order")
    address = models.ForeignKey(Address, help_text="Delivery Address")
    created_date = models.DateTimeField(auto_now=True, help_text="Date the order was created")
    delivery_date = models.DateField(help_text="Date the party would like the order delivered")
    order_status = models.CharField(max_length=1, choices=ORDER_STATUS, help_text="current status of the order")
    invoice_date = models.DateTimeField(null=True, blank=True, help_text="Date the order was invoiced")

    def get_next_order_number(self):
        """
        Gets the next order number that should be used for a new record
        """
        last_order = Order.objects.all().order_by('-order_number').first()
        if last_order != None:
            return last_order.order_number + 1
        else:
            return 1

    def __str__(self):
        """
        The Description defined when viewing as a foreign key field
        """
        return '%s %s' % (self.order_number, self.order_status)


class OrderLine(models.Model):
    """
    Stores an Order Line Record including relevant item information and pricing information,
    related to :model:`order.Order` and :model:`product.Item`.
    """
    order_line_id = models.IntegerField(help_text="Id of the current line (unique)")
    order_number = models.ForeignKey(Order, help_text="Link to the order that this line belongs to")
    item_id = models.ForeignKey(Item, help_text="Link to the item that is on this line")
    quantity = models.IntegerField(help_text="Quantity to deliver")
    price = models.FloatField(help_text="price to charge the party for this line")
    discount_price = models.FloatField(help_text="the price minus any discount found for this party")
    unit = models.CharField(max_length=10, help_text="the unit that this item comes in")

    def get_next_line_id(self):
        """
        Gets the next order line number that should be used for a new record
        """
        last_line = OrderLine.objects.filter(order_number=self.order_number).order_by('-order_line_id').first()
        if last_line != None:
            return last_line.order_line_id + 1
        else:
            return 1


class Discounts(models.Model):
    """
    Stores a Discount Record including relevant item and party information and the percentage discount a customer gets,
    related to :model:`party.Party`.
    """
    account_number = models.ForeignKey(Party, help_text="Link to the party that this discount belongs to")
    product_category = models.CharField(max_length=30, null=True, blank=True, help_text="Category of the product")
    item_id = models.IntegerField(null=True, blank=True, help_text="Item id of the product")
    quantity = models.IntegerField(null=True, blank=True, help_text="Quantity that this discount starts at")
    start_date = models.DateTimeField(help_text="The date the discount will begin to take effect")
    end_date = models.DateTimeField(null=True, blank=True, help_text="The date the discount will no longer take effect")
    value = models.FloatField(null=True, blank=True, help_text="the value of the discount between 0 and 1")





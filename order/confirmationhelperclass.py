from order.models import Order
from order.models import OrderLine
from product.models import Item
from stock.models import Inventory
from order.confirmationresult import *


def confirmorder(corder):
    result = ConfirmResult()
    # Order = OrderLine.objects.first(order_number=corder)

    # for sl in OrderLine.objects.filter(order_number=corder):
    #    prod = Item.objects.first(item_id=sl.item_id)
    #    inv = Inventory.objects.first(item_id=sl.item_id)
    #
    #    if prod is None or inv is None:
    #        result.confirmation_status = "Not Ordered"
    #        result.add_error(result, "Error: product or inventory record not found")
    #    else:
    #        if inv.available_qty >= sl.quantity:
    #            Inventory.reserve_qty(inv, sl.quantity)
    #            result.confirmation_status = "Ordered"

    #        elif inv.available_qty < sl.quantity:
    #            Inventory.add_ordered_qty(inv, sl.quantity)
    #            result.confirmation_status = "Not Ordered"
    #            result.add_error(result, "Error: Not enough Stock Available, a fulfilment order has been placed")

    # test return
    result.confirmation_status = "Not Ordered"
    result.add_error("Error: product or inventory record not found")

    return result



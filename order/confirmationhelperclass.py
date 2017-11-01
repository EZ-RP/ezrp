from order.models import Order
from order.models import OrderLine
from product.models import Item
from stock.models import Inventory


def confirmorder(corder):
    result = {"N/A", "N/A", "N/A"}

    for sl in OrderLine.objects.filter(order_number=corder):
        prod = Item.objects.first(item_id=sl.item_id)
        inv = Inventory.objects.first(item_id=sl.item_id)

        if prod is None or inv is None:
            result[0] = "Not Ordered"
            result[1] = "Error: product or inventory record not found"
        else:
            if inv.available_qty >= sl.quantity:
                Inventory.reserve_qty(inv, sl.quantity)
                result[0] = "Ordered"

            elif inv.available_qty < sl.quantity:
                Inventory.add_ordered_qty(inv, sl.quantity)
                result[0] = "Not Ordered"
                result[1] = "Error: Not enough Stock Available, a fulfilment order has been placed"

    # print(sl.order_line_id)

    return result



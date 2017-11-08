import time
from order.models import *
from order.models import *
from product.models import Item
from stock.models import Inventory
from order.confirmationresult import *


def confirmorder(corder):
    result = ConfirmResult()
    tdate = time.strftime("%Y-%m-%d")

    if corder.order_status == "C":
        for sl in OrderLine.objects.filter(order_number=corder):
            prod = Item.objects.filter(id=sl.item_id.id).first()
            inv = Inventory.objects.filter(item_id=sl.item_id.id).first()

            if prod is None or inv is None:
                result.add_error("Error: product or inventory record not found")
            else:
                if corder.order_type == "S":
                    if inv.available_qty >= sl.quantity:
                        Inventory.reserve_qty(inv, sl.quantity)

                    elif inv.available_qty < sl.quantity:
                        if prod.fulfilment_type == "P":
                            fulord = Order(account_number=corder.account_number, order_type='P')
                            fulord.order_number = Order.get_next_order_number(fulord)
                            fulord.address = corder.address
                            fulord.created_date = tdate
                            fulord.delivery_date = tdate
                            fulord.order_status = "C"
                            fulord.save()
                            fulline = OrderLine(order_number=fulord)
                            fulline.order_line_id = OrderLine.get_next_line_id(fulline)
                            fulline.item_id = sl.item_id
                            fulline.quantity = sl.quantity
                            fulline.price = sl.price
                            fulline.discount_price = sl.price
                            fulline.unit = sl.unit
                            fulline.save()
                        elif prod.fulfilment_type == "M":
                            fulord = Order(account_number=corder.account_number, order_type='M')
                            fulord.order_number = Order.get_next_order_number(fulord)
                            fulord.address = corder.address
                            fulord.created_date = tdate
                            fulord.delivery_date = tdate
                            fulord.order_status = "C"
                            fulord.save()
                            fulline = OrderLine(order_number=fulord)
                            fulline.order_line_id = OrderLine.get_next_line_id(fulline)
                            fulline.item_id = sl.item_id
                            fulline.quantity = sl.quantity
                            fulline.price = sl.price
                            fulline.discount_price = sl.price
                            fulline.unit = sl.unit
                            fulline.save()

                        result.add_error("Error: Not enough Stock Available a fulfilment order has been placed")
                else:
                    Inventory.add_ordered_qty(inv, sl.quantity)

        if len(result.confirmation_errors) > 0:
            result.confirmation_status = "Not Ordered"
        else:
            result.confirmation_status = "Ordered"
    else:
        result.confirmation_status = "Not Ordered"
        result.add_error("Error: Order is already confirmed")

    # test return
    # result.confirmation_status = "Not Ordered"
    # result.add_error("Error: product or inventory record not found")

    return result


def invoiceorder(iorder):
    result = ConfirmResult()

    if iorder.order_status == "O":
        for sl in OrderLine.objects.filter(order_number=iorder):
            prod = Item.objects.filter(id=sl.item_id.id).first()
            inv = Inventory.objects.filter(item_id=sl.item_id.id).first()

            if prod is None or inv is None:
                result.add_error("Error: product or inventory record not found")
            else:
                if iorder.order_type == "S":
                    Inventory.remove_reserved_qty(inv, sl.quantity)
                else:
                    Inventory.add_ordered_to_available(inv, sl.quantity)

            if len(result.confirmation_errors) > 0:
                result.confirmation_status = "Not Invoiced"
            else:
                result.confirmation_status = "Invoiced"
    else:
        result.confirmation_status = "Not Invoiced"
        result.add_error("Error: Order is already invoiced")

    return result

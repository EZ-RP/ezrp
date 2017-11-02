from django.shortcuts import render
from stock.models import Inventory
from .forms import InvForm
from django_tables2 import RequestConfig
from stock.tables import StockTable
from django.http import HttpResponse
# Create your views here.


def main(request):
    return render(request, 'stock/Stock.html')


def available(request):
    items = StockTable(Inventory.objects.all())
    RequestConfig(request).configure(items)
    return render(request, 'stock/all_available.html', {'available': items})
    # return render(request, 'stock/all_available.html', {'available': Inventory.objects.all()})


def stockform(request):
    if request.method == "POST":
        form = InvForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = InvForm()
    return render(request, 'stock/stock_form.html', {'form': form})


def stock_delete(request, item_id):
    Inventory.objects.get(item_id=item_id).delete()
    items = StockTable(Inventory.objects.all())
    RequestConfig(request).configure(items)
    return render(request, 'stock/all_available.html', {'available': items})


def stock_edit(request, order_number):

    show_line_form = False

    if request.GET.get('confirm_order'):
        confirmorder(Order.objects.first(order_number=order_number))

    if request.GET.get('add_line'):
        show_line_form = True

    if request.method == "POST":
        form_orderlines = LineForm(request.POST)

        if form_orderlines.is_valid():

            order_line = form_orderlines.save(commit=False)
            order_line.order_number = Order.objects.get(order_number=order_number)
            order_line.order_line_id = OrderLine.get_next_line_id(order_line)

            # orde = Order.objects.first(order_number=order_number)
            # dsc = Discounts.objects.first(account_number=orde.account_number, item_id=order_line.item_id)

            # if dsc is None:
            #    order_line.discount_price = order_line.price
            # else:
            prc = order_line.price
            # dscp = dsc.
            order_line.discount_price = prc * (1 - 0.1)

            order_line.save()
            form_orderlines = LineForm()
            show_line_form = False

            singlesale = Order.objects.get(order_number=order_number, order_type='S')
            form_order = OrderForm(instance=singlesale)
            saleslines = OrderLine.objects.filter(order_number=order_number)
    else:

        singlesale = Order.objects.get(order_number=order_number, order_type='S')
        form_order = OrderForm(instance=singlesale)
        form_orderlines = LineForm()
        saleslines  = OrderLine.objects.filter(order_number=singlesale)

        if not show_line_form:

            if saleslines.exists():

                show_line_form = False

            else:

                show_line_form = True

    return render(request, 'order/Sales/sale.html', {'form_sale': form_order, 'form_orderline': form_orderlines, 'saleslines': saleslines, 'show_line_form': show_line_form})

from django.shortcuts import render
from django.views.generic import ListView
from order.models import Order
from order.models import OrderLine
from order.models import Discounts
from .modelforms import OrderForm
from .modelforms import LineForm
from .modelforms import DiscountForm
from django.http import HttpResponse
from django_tables2 import RequestConfig
from order.tables import SaleTable
from order.tables import SalesLineTable
from order.tables import DiscountTable
from order.confirmationhelperclass import confirmorder


# Sales views


def sales(request):
    return render(request, 'order/Sales/sales.html')


def all_sales(request):
    saless = SaleTable(Order.objects.filter(order_type="S"))
    RequestConfig(request).configure(saless)
    return render(request, 'order/Sales/all_salesOrders.html', {'sales': saless})


def all_saleslines(request):
    salesliness = SalesLineTable(
        OrderLine.objects.filter(
            order_number=Order.objects.values_list(
                'order_number').filter(order_type="S")))
    RequestConfig(request).configure(salesliness)
    return render(request, 'order/Sales/all_salesLines.html', {'saleslines': salesliness})
    # return render(request, 'order/Sales/all_salesLines.html',
                  # {'saleslines': OrderLine.objects.all()})


def sale(request, order_number):
    singlesale = Order.objects.get(order_number=order_number, order_type='S')
    form_order = OrderForm(instance=singlesale)
    return render(request, 'order/Sales/sale.html', {'form_sale': form_order})


def sale_edit(request, order_number):

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


def sale_delete(request, order_number):
    Order.objects.get(order_number=order_number).delete()
    saless = SaleTable(Order.objects.filter(order_type="S"))
    RequestConfig(request).configure(saless)
    return render(request, 'order/Sales/all_salesOrders.html', {'sales': saless})


def salesline_delete(request, lineid):
    OrderLine.objects.get(id=lineid).delete()
    salesliness = SalesLineTable(
        OrderLine.objects.filter(
            order_number=Order.objects.values_list(
                'order_number').filter(order_type="S")))
    RequestConfig(request).configure(salesliness)
    return render(request, 'order/Sales/all_salesOrders.html', {'saleliness': salesliness})


def sale_new(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.order_type = 'S'
            order.save()
            form = OrderForm()
    else:
        form = OrderForm()
    return render(request, 'order/Sales/sale_new.html', {'form': form})


def saleline_new(request):
    if request.method == "POST":
        form = LineForm(request.POST)
        if form.is_valid():
            orderline = form.save(commit=False)
            orderline.order_number = Order.objects.get(order_number=1)
            if OrderLine.objects.count() > 0:
                orderline.order_line_id = OrderLine.objects.latest('order_line_id').get_latest_by(order_number=orderline.order_number)
            else:
                orderline.order_line_id = 1
            orderline.save()
            form = LineForm()
    else:
        form = LineForm()
    return render(request, 'order/Sales/saleline_new.html', {'form': form})


def sale_view(request):
    if request.method == "POST":
        form_order = OrderForm(request.GET)
        form_orderline = LineForm(request.POST)
        if form_order.is_valid() and form_orderline.is_valid():
            orderline = form_orderline.save(commit=False)
            if OrderLine.objects.count() > 0:
                lineid = OrderLine.objects.latest('order_line_id').get_latest_by(order_number=orderline.order_number)
                orderline.order_line_id = lineid
            else:
                orderline.order_line_id = 1
            orderline.order_number = form_order.order_number
            orderline.unit = "ea"
            orderline.save()
    else:
        form_order = OrderForm(request.GET)
        form_orderline = LineForm()
    return render(request, 'order/Sales/sale_view.html', {'form_order': form_order, 'form_orderline': form_orderline})


# Purchase views


def purchases(request):
    return render(request, 'order/Purchases/purchases.html')


def all_purchases(request):
    return render(request, 'order/Purchases/all_purchaseOrders.html',
                  {'purchases': Order.objects.filter(order_type="P")})


# Production views


def production(request):
    return render(request, 'order/Production/production.html')


def all_production(request):
    return render(request, 'order/Production/all_productionOrders.html',
                  {'production': Order.objects.filter(order_type="M")})


# Discount views


def setup(request):
    return render(request, 'order/orderSetup.html')


def all_discounts(request):
    # return render(request, 'order/Sales/all_discounts.html',
    #               {'discounts': Discounts.objects.all()})
    discs = DiscountTable(Discounts.objects.all())
    RequestConfig(request).configure(discs)
    return render(request, 'order/all_discounts.html', {'discounts': discs})


def new_discount(request):
    if request.method == "POST":
        form = DiscountForm(request.POST)
        if form.is_valid():
            form.save()
            form = DiscountForm()
    else:
        form = DiscountForm()
    return render(request, 'order/new_discount.html', {'form': form})


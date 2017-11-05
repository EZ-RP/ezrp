import time
from django.shortcuts import render
from django_tables2 import RequestConfig
from order.confirmationhelperclass import confirmorder
from django.contrib import messages
from .models import *
from .modelforms import *
from .tables import *
from .filters import *


# Main Page
def orders(request):
    return render(request, 'order/ordersMain.html')


# Sales views
def sales(request):
    return render(request, 'order/Sales/sales.html')


def all_sales(request):
    filter = OrderFilter(request.GET, Order.objects.filter(order_type="S"))
    saless = OrderTable(filter.qs)
    RequestConfig(request).configure(saless)
    return render(request, 'order/Sales/all_salesOrders.html', {'sales': saless, 'filter': filter})


def all_saleslines(request):
    salesliness = OrderLineTable(
        OrderLine.objects.filter(
            order_number=Order.objects.values_list(
                'order_number').filter(order_type="S")))
    RequestConfig(request).configure(salesliness)
    return render(request, 'order/Sales/all_salesLines.html', {'saleslines': salesliness})


def sale(request, order_number):
    singlesale = Order.objects.get(order_number=order_number, order_type='S')
    form_order = OrderForm(instance=singlesale)
    return render(request, 'order/Sales/sale.html', {'form_sale': form_order})


def sale_edit(request, order_number):

    show_line_form = False
    storage = messages.get_messages(request)
    storage.used = True

    if request.GET.get('confirm_order'):
        ord = Order.objects.get(order_number=order_number)
        result = confirmorder(ord)

        if result.confirmation_status == "Ordered":
            ord.order_status = "O"
        else:
            for er in result.confirmation_errors:
                messages.error(request, er, extra_tags='email')

    if request.GET.get('add_line'):
        show_line_form = True

    if request.method == "POST":
        form_orderlines = LineForm(request.POST)

        if form_orderlines.is_valid():

            order_line = form_orderlines.save(commit=False)
            order_line.order_number = Order.objects.get(order_number=order_number)
            order_line.order_line_id = OrderLine.get_next_line_id(order_line)

            orde = Order.objects.get(order_number=order_number)
            tdate = time.strftime("%Y/%m/%d")

            if Discounts.objects.filter(account_number=orde.account_number, item_id=order_line.item_id.id,
                                        startdate__lte=tdate, enddate__gt=tdate).exists():
                dsc = Discounts.objects.get(account_number=orde.account_number, item_id=order_line.item_id.id,
                                            startdate__lte=tdate, enddate__gt=tdate)
                prc = order_line.price
                dscp = dsc.value
                order_line.discount_price = prc * (1 - dscp)
            else:
                order_line.discount_price = order_line.price

            order_line.unit = order_line.item_id.unit
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
    saless = OrderTable(Order.objects.filter(order_type="S"))
    RequestConfig(request).configure(saless)
    return render(request, 'order/Sales/all_salesOrders.html', {'sales': saless})


def salesline_delete(request, lineid):
    OrderLine.objects.get(id=lineid).delete()
    salesliness = OrderLineTable(
        OrderLine.objects.filter(
            order_number=Order.objects.values_list(
                'order_number').filter(order_type="S")))
    RequestConfig(request).configure(salesliness)
    return render(request, 'order/Sales/all_salesLines.html', {'saleliness': salesliness})


def sale_new(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.order_number = Order.get_next_order_number(order)
            order.order_type = 'S'
            order.save()
            form = OrderForm()
    else:
        form = OrderForm()
    return render(request, 'order/Sales/sale_new.html', {'form': form})


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
    filter = OrderFilter(request.GET, Order.objects.filter(order_type="P"))
    purchs = OrderTable(filter.qs)
    RequestConfig(request).configure(purchs)
    return render(request, 'order/Purchases/all_purchOrders.html',{'purchases': purchs, 'filter': filter})


def all_purchlines(request):
    purchliness = OrderLineTable(
        OrderLine.objects.filter(
            order_number=Order.objects.values_list(
                'order_number').filter(order_type="P")))
    RequestConfig(request).configure(purchliness)
    return render(request, 'order/Purchases/all_purchLines.html', {'purchlines': purchliness})


def purch_delete(request, order_number):
    Order.objects.get(order_number=order_number).delete()
    purchs = OrderTable(Order.objects.filter(order_type="P"))
    RequestConfig(request).configure(purchs)
    return render(request, 'order/Purchases/all_purchOrders.html', {'purch': purchs})


def purchline_delete(request, lineid):
    OrderLine.objects.get(id=lineid).delete()
    purchliness = OrderLineTable(
        OrderLine.objects.filter(
            order_number=Order.objects.values_list(
                'order_number').filter(order_type="P")))
    RequestConfig(request).configure(purchliness)
    return render(request, 'order/Purchases/all_purchLines.html', {'purchliness': purchliness})


def purch_new(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.order_number = Order.get_next_order_number(order)
            order.order_type = 'P'
            order.save()
            form = OrderForm()
    else:
        form = OrderForm()
    return render(request, 'order/Purchases/new_purch.html', {'form': form})


def purch(request, order_number):
    singlepurch = Order.objects.get(order_number=order_number, order_type='P')
    form_order = OrderForm(instance=singlepurch)
    return render(request, 'order/Purchases/purch.html', {'form_purch': form_order})


def purch_edit(request, order_number):

    show_line_form = False
    storage = messages.get_messages(request)
    storage.used = True

    if request.GET.get('confirm_order'):
        ord = Order.objects.get(order_number=order_number)
        result = confirmorder(ord)

        if result.confirmation_status == "Ordered":
            ord.order_status = "O"
        else:
            for er in result.confirmation_errors:
                messages.error(request, er, extra_tags='email')

    if request.GET.get('add_line'):
        show_line_form = True

    if request.method == "POST":
        form_orderlines = LineForm(request.POST)

        if form_orderlines.is_valid():

            order_line = form_orderlines.save(commit=False)
            order_line.order_number = Order.objects.get(order_number=order_number)
            order_line.order_line_id = OrderLine.get_next_line_id(order_line)
            order_line.discount_price = order_line.price
            order_line.unit = order_line.item_id.unit
            order_line.save()
            form_orderlines = LineForm()
            show_line_form = False

            singlepurch = Order.objects.get(order_number=order_number, order_type='P')
            form_order = OrderForm(instance=singlepurch)
            purchlines = OrderLine.objects.filter(order_number=order_number)
    else:

        singlepurch = Order.objects.get(order_number=order_number, order_type='P')
        form_order = OrderForm(instance=singlepurch)
        form_orderlines = LineForm()
        purchlines = OrderLine.objects.filter(order_number=singlepurch)

        if not show_line_form:

            if purchlines.exists():

                show_line_form = False

            else:

                show_line_form = True

    return render(request, 'order/Purchases/purch.html', {'form_purch': form_order, 'form_orderline': form_orderlines, 'purchlines': purchlines, 'show_line_form': show_line_form})


# Production views
def production(request):
    return render(request, 'order/Production/production.html')


def all_production(request):
    filter = OrderFilter(request.GET, Order.objects.filter(order_type="M"))
    prods = OrderTable(filter.qs)
    RequestConfig(request).configure(prods)
    return render(request, 'order/Production/all_prodOrders.html', {'production': prods, 'filter': filter})


def all_prodlines(request):
    prodliness = OrderLineTable(
        OrderLine.objects.filter(
            order_number=Order.objects.values_list(
                'order_number').filter(order_type="M")))
    RequestConfig(request).configure(prodliness)
    return render(request, 'order/Production/all_prodLines.html', {'prodlines': prodliness})


def prod_delete(request, order_number):
    Order.objects.get(order_number=order_number).delete()
    prods = OrderTable(Order.objects.filter(order_type="M"))
    RequestConfig(request).configure(prods)
    return render(request, 'order/Production/all_prodOrders.html', {'prod': prods})


def prodline_delete(request, lineid):
    OrderLine.objects.get(id=lineid).delete()
    prodliness = OrderLineTable(
        OrderLine.objects.filter(
            order_number=Order.objects.values_list(
                'order_number').filter(order_type="M")))
    RequestConfig(request).configure(prodliness)
    return render(request, 'order/Production/all_prodLines.html', {'prodliness': prodliness})


def prod_new(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.order_number = Order.get_next_order_number(order)
            order.order_type = 'M'
            order.save()
            form = OrderForm()
    else:
        form = OrderForm()
    return render(request, 'order/Production/new_prod.html', {'form': form})


def prod(request, order_number):
    singleprod = Order.objects.get(order_number=order_number, order_type='M')
    form_order = OrderForm(instance=singleprod)
    return render(request, 'order/Production/prod.html', {'form_prod': form_order})


def prod_edit(request, order_number):

    show_line_form = False
    storage = messages.get_messages(request)
    storage.used = True

    if request.GET.get('confirm_order'):
        ord = Order.objects.get(order_number=order_number)
        result = confirmorder(ord)

        if result.confirmation_status == "Ordered":
            ord.order_status = "O"
        else:
            for er in result.confirmation_errors:
                messages.error(request, er, extra_tags='email')

    if request.GET.get('add_line'):
        show_line_form = True

    if request.method == "POST":
        form_orderlines = LineForm(request.POST)

        if form_orderlines.is_valid():

            order_line = form_orderlines.save(commit=False)
            order_line.order_number = Order.objects.get(order_number=order_number)
            order_line.order_line_id = OrderLine.get_next_line_id(order_line)
            order_line.discount_price = order_line.price
            order_line.unit = order_line.item_id.unit
            order_line.save()
            form_orderlines = LineForm()
            show_line_form = False

            singleprod = Order.objects.get(order_number=order_number, order_type='M')
            form_order = OrderForm(instance=singleprod)
            prodlines = OrderLine.objects.filter(order_number=order_number)
    else:

        singleprod = Order.objects.get(order_number=order_number, order_type='M')
        form_order = OrderForm(instance=singleprod)
        form_orderlines = LineForm()
        prodlines = OrderLine.objects.filter(order_number=singleprod)

        if not show_line_form:

            if prodlines.exists():

                show_line_form = False

            else:

                show_line_form = True

    return render(request, 'order/Production/sale.html', {'form_prod': form_order, 'form_orderline': form_orderlines, 'prodlines': prodlines, 'show_line_form': show_line_form})


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
    storage = messages.get_messages(request)
    storage.used = True

    if request.method == "POST":
        form = DiscountForm(request.POST)
        if form.is_valid():
            disc = form.save(commit=False)

            if disc.value < 1:
                disc.save()
            else:
                messages.error(request, "Discount not saved, check value is less than 1 or less than 100%",
                               extra_tags='email')

            form = DiscountForm()
    else:
        form = DiscountForm()
    return render(request, 'order/new_discount.html', {'form': form})


def discount_delete(request, lineid):
    Discounts.objects.get(id=lineid).delete()
    discs = DiscountTable(Discounts.objects.all())
    RequestConfig(request).configure(discs)
    return render(request, 'order/all_discounts.html', {'discounts': discs})


def discount_edit(request, lineid):
    if request.method == "POST":
        disc = Discounts.objects.get(id=lineid)
        form_disc = DiscountForm(request.POST, instance=disc)
        if form_disc.is_valid():
            form_disc.save(commit=True)

            discs = DiscountTable(Discounts.objects.all())
            RequestConfig(request).configure(discs)
            return render(request, 'order/all_discounts.html', {'discounts': discs})
    else:
        singledisc = Discounts.objects.get(id=lineid)
        form_disc = DiscountForm(instance=singledisc)
        return render(request, 'order/new_discount.html', {'form': form_disc})


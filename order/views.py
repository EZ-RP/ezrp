import time
from django.shortcuts import render
from django_tables2 import RequestConfig
from django.contrib import messages
from .models import *
from .modelforms import *
from .tables import *
from .filters import *
from .confirmationhelperclass import *


# Main Page
def orders(request):
    """
    Display the orders menu.

    **Template:**

    :template:`order/ordersMain.html`
    """
    return render(request, 'order/ordersMain.html')


# Sales views
def sales(request):
    """
    Display the Sales menu.

    **Template:**

    :template:`order/Sales/sales.html`
    """
    return render(request, 'order/Sales/sales.html')


def all_sales(request):
    """
    Display all :model:`order.Order` of type sales.

    ``sales``
        A query set of :model:`order.Order`.

    ``filter``
        The relevant filter object :model:`order.OrderFilter`.

    **Template:**

    :template:`order/Sales/all_salesOrders.html`
    """
    filt = OrderFilter(request.GET, Order.objects.filter(order_type="S"))
    saless = SalesTable(filt.qs)
    RequestConfig(request).configure(saless)
    return render(request, 'order/Sales/all_salesOrders.html', {'sales': saless, 'filter': filt})


def all_saleslines(request):
    """
    Display all :model:`order.OrderLine` of type sales.

    ``saleslines``
        A query set of :model:`order.OrderLine`.

    **Template:**

    :template:`order/Sales/all_salesLines.html`
    """
    salesliness = SalesLineTable(OrderLine.objects.filter(order_number__order_type="S"))
    RequestConfig(request).configure(salesliness)
    return render(request, 'order/Sales/all_salesLines.html', {'saleslines': salesliness})


def sale(request, order_number):
    """
    Create a new instance of :model:`order.Order` of type sales.

    ``form_sale``
        An instance of :model:`order.OrderForm`.

    **Template:**

    :template:`order/Sales/sale.html`
    """
    singlesale = Order.objects.get(order_number=order_number, order_type='S')
    form_order = OrderForm(instance=singlesale)
    return render(request, 'order/Sales/sale.html', {'form_sale': form_order})


def sale_edit(request, order_number):
    """
    Edit/Confirm/Invoice an instance of :model:`order.Order` of type sales.

    ``form_sale``
        An instance of :model:`order.OrderForm`.

    ``form_orderline``
        An instance of :model:`order.OrderLineForm`.

    ``saleslines``
        A query set of :model:`order.OrderLine`.

    ``show_line_form``
        A boolean to determine if the line form should be shown.

    **Template:**

    :template:`order/Sales/sale.html`
    """
    show_line_form = False
    storage = messages.get_messages(request)
    storage.used = True

    if request.GET.get('confirm_order'):
        cord = Order.objects.get(order_number=order_number)
        result = confirmorder(cord)

        if result.confirmation_status == "Ordered":
            cord.order_status = "O"
            cord.save()
        else:
            for er in result.confirmation_errors:
                messages.error(request, er, extra_tags='email')

    if request.GET.get('invoice_order'):
        iord = Order.objects.get(order_number=order_number)
        result = invoiceorder(iord)

        if result.confirmation_status == "Invoiced":
            iord.order_status = "I"
            iord.invoice_date = time.strftime("%Y-%m-%dT%H:%M:%S")
            iord.save()
        else:
            for er in result.confirmation_errors:
                messages.error(request, er, extra_tags='email')

    if request.GET.get('add_line'):
        aord = Order.objects.get(order_number=order_number)
        if aord.order_status == "C":
            show_line_form = True
        else:
            messages.error(request, "Cannot add lines to confirmed or invoiced orders", extra_tags='email')

    if request.method == "POST":
        form_orderlines = LineForm(request.POST)

        if form_orderlines.is_valid():

            order_line = form_orderlines.save(commit=False)
            order_line.order_number = Order.objects.get(order_number=order_number)
            order_line.order_line_id = OrderLine.get_next_line_id(order_line)

            orde = Order.objects.get(order_number=order_number)
            tdate = time.strftime("%Y-%m-%d")

            if Discounts.objects.filter(account_number=orde.account_number, item_id=order_line.item_id.id,
                                        start_date__lte=tdate, end_date__gt=tdate,
                                        quantity__lte=order_line.quantity).exists():
                dsc = Discounts.objects.get(account_number=orde.account_number, item_id=order_line.item_id.id,
                                            start_date__lte=tdate, end_date__gt=tdate,
                                            quantity__lte=order_line.quantity)
                prc = order_line.price
                dscp = dsc.value
                order_line.discount_price = prc * (1 - dscp)
            else:
                order_line.discount_price = order_line.price

            order_line.unit = order_line.item_id.unit
            order_line.save()
            form_orderlines = LineForm()
            show_line_form = False

            singlesale = Order.objects.get(order_number=order_number)
            form_order = OrderForm(instance=singlesale)
            saleslines = OrderLine.objects.filter(order_number=singlesale)
    else:

        singlesale = Order.objects.get(order_number=order_number)
        form_order = OrderForm(instance=singlesale)
        form_orderlines = LineForm()
        saleslines = OrderLine.objects.filter(order_number=singlesale)

        if not show_line_form:

            if saleslines.exists():

                show_line_form = False

            else:

                show_line_form = True

    return render(request, 'order/Sales/sale.html', {'form_sale': form_order, 'form_orderline': form_orderlines,
                                                     'saleslines': saleslines, 'show_line_form': show_line_form})


def sale_delete(request, order_number):
    """
    Delete an object :model:`order.Order` of type sales.

    ``sales``
        A query set of :model:`order.Order`.

    ``filter``
        The relevant filter object :model:`order.OrderFilter`.

    **Template:**

    :template:`order/Sales/all_salesOrders.html`
    """
    storage = messages.get_messages(request)
    storage.used = True
    delorder = Order.objects.get(order_number=order_number)

    if delorder.order_status == "C":
        delorder.delete()
    else:
        messages.error(request, "Cannot delete confirmed or invoiced orders", extra_tags='email')

    filt = OrderFilter(request.GET, Order.objects.filter(order_type="S"))
    saless = SalesTable(filt.qs)
    RequestConfig(request).configure(saless)
    return render(request, 'order/Sales/all_salesOrders.html', {'sales': saless, 'filter': filt})


def salesline_delete(request, sid):
    """
    Delete an object :model:`order.OrderLine` from a sale.

    ``saleslines``
        A query set of :model:`order.OrderLine`.

    **Template:**

    :template:`order/Sales/all_salesLines.html`
    """
    storage = messages.get_messages(request)
    storage.used = True
    delline = OrderLine.objects.get(id=sid)

    if delline.order_number.order_status == "C":
        delline.delete()
    else:
        messages.error(request, "Cannot delete lines from a confirmed or invoiced order", extra_tags='email')

    salesliness = SalesLineTable(OrderLine.objects.filter(order_number__order_type="S"))
    RequestConfig(request).configure(salesliness)
    return render(request, 'order/Sales/all_salesLines.html', {'saleslines': salesliness})


def sale_new(request):
    """
    Create a new instance of :model:`order.Order` of type sales.

    ``form``
        An instance of :model:`order.OrderForm`.

    **Template:**

    :template:`order/Sales/sale_new.html`
    """
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.order_number = Order.get_next_order_number(order)
            order.order_type = 'S'
            order.order_status = "C"
            order.save()
            form = OrderForm()
            form.fields['account_number'].queryset = Party.objects.filter(party_type='C')
    else:
        form = OrderForm()
        form.fields['account_number'].queryset = Party.objects.filter(party_type='C')
    return render(request, 'order/Sales/sale_new.html', {'form': form})


# Purchase views
def purchases(request):
    """
    Display the Purchases menu.

    **Template:**

    :template:`order/Purchases/purchases.html`
    """
    return render(request, 'order/Purchases/purchases.html')


def all_purchases(request):
    """
    Display all :model:`order.Order` of type Purchase.

    ``purchases``
        A query set of :model:`order.Order`.

    ``filter``
        The relevant filter object :model:`order.OrderFilter`.

    **Template:**

    :template:`order/Purchases/all_purchOrders.html`
    """
    filt = OrderFilter(request.GET, Order.objects.filter(order_type="P"))
    purchs = PurchTable(filt.qs)
    RequestConfig(request).configure(purchs)
    return render(request, 'order/Purchases/all_purchOrders.html', {'purchases': purchs, 'filter': filt})


def all_purchlines(request):
    """
    Display all :model:`order.OrderLine` of type Purchase.

    ``purchlines``
        A query set of :model:`order.OrderLine`.

    **Template:**

    :template:`order/Purchases/all_purchLines.html`
    """
    purchliness = PurchLineTable(OrderLine.objects.filter(order_number__order_type="P"))
    RequestConfig(request).configure(purchliness)
    return render(request, 'order/Purchases/all_purchLines.html', {'purchlines': purchliness})


def purch_delete(request, order_number):
    """
    Delete an object :model:`order.Order` of type Purchase.

    ``purchases``
        A query set of :model:`order.Order`.

    ``filter``
        The relevant filter object :model:`order.OrderFilter`.

    **Template:**

    :template:`order/Purchases/all_purchOrders.html`
    """
    storage = messages.get_messages(request)
    storage.used = True
    delorder = Order.objects.get(order_number=order_number)

    if delorder.order_status == "C":
        delorder.delete()
    else:
        messages.error(request, "Cannot delete confirmed or invoiced orders", extra_tags='email')

    filt = OrderFilter(request.GET, Order.objects.filter(order_type="P"))
    purchs = PurchTable(filt.qs)
    RequestConfig(request).configure(purchs)
    return render(request, 'order/Purchases/all_purchOrders.html', {'purchases': purchs, 'filter': filt})


def purchline_delete(request, pid):
    """
    Delete an object :model:`order.OrderLine` from a purchase order.

    ``purchlines``
        A query set of :model:`order.OrderLine`.

    **Template:**

    :template:`order/Purchases/all_purchLines.html`
    """
    storage = messages.get_messages(request)
    storage.used = True
    delline = OrderLine.objects.get(id=pid)

    if delline.order_number.order_status == "C":
        delline.delete()
    else:
        messages.error(request, "Cannot delete lines from a confirmed or invoiced order", extra_tags='email')

    purchliness = PurchLineTable(OrderLine.objects.filter(order_number__order_type="P"))
    RequestConfig(request).configure(purchliness)
    return render(request, 'order/Purchases/all_purchLines.html', {'purchlines': purchliness})


def purch_new(request):
    """
    Create a new instance of :model:`order.Order` of type Purchase.

    ``form``
        An instance of :model:`order.OrderForm`.

    **Template:**

    :template:`order/Purchases/new_purch.html`
    """
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.order_number = Order.get_next_order_number(order)
            order.order_type = 'P'
            order.order_status = "C"
            order.save()
            form = OrderForm()
    else:
        form = OrderForm()
    return render(request, 'order/Purchases/new_purch.html', {'form': form})


def purch(request, order_number):
    """
    Create a new instance of :model:`order.Order` of type Purchase.

    ``form_purch``
        An instance of :model:`order.OrderForm`.

    **Template:**

    :template:`order/Purchases/Purch.html`
    """
    singlepurch = Order.objects.get(order_number=order_number, order_type='P')
    form_order = OrderForm(instance=singlepurch)
    return render(request, 'order/Purchases/Purch.html', {'form_purch': form_order})


def purch_edit(request, order_number):
    """
    Edit/Confirm/Invoice an instance of :model:`order.Order` of type Purchase.

    ``form_purch``
        An instance of :model:`order.OrderForm`.

    ``form_orderline``
        An instance of :model:`order.OrderLineForm`.

    ``purchlines``
        A query set of :model:`order.OrderLine`.

    ``show_line_form``
        A boolean to determine if the line form should be shown.

    **Template:**

    :template:`order/Purchases/Purch.html`
    """

    show_line_form = False
    storage = messages.get_messages(request)
    storage.used = True

    if request.GET.get('confirm_order'):
        ord = Order.objects.get(order_number=order_number)
        result = confirmorder(ord)

        if result.confirmation_status == "Ordered":
            ord.order_status = "O"
            ord.save()
        else:
            for er in result.confirmation_errors:
                messages.error(request, er, extra_tags='email')

    if request.GET.get('invoice_order'):
        iord = Order.objects.get(order_number=order_number)
        result = invoiceorder(iord)

        if result.confirmation_status == "Invoiced":
            iord.order_status = "I"
            iord.invoice_date = time.strftime("%Y-%m-%dT%H:%M:%S")
            iord.save()
        else:
            for er in result.confirmation_errors:
                messages.error(request, er, extra_tags='email')

    if request.GET.get('add_line'):
        aord = Order.objects.get(order_number=order_number)
        if aord.order_status == "C":
            show_line_form = True
        else:
            messages.error(request, "Cannot add lines to confirmed or invoiced orders", extra_tags='email')

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
            purchlines = OrderLine.objects.filter(order_number=singlepurch)
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

    return render(request, 'order/Purchases/Purch.html', {'form_purch': form_order, 'form_orderline': form_orderlines,
                                                          'purchlines': purchlines, 'show_line_form': show_line_form})


# Production views
def production(request):
    """
    Display the Production menu.

    **Template:**

    :template:`order/Production/production.html`
    """
    return render(request, 'order/Production/production.html')


def all_production(request):
    """
    Display all :model:`order.Order` of type Production.

    ``production``
        A query set of :model:`order.Order`.

    ``filter``
        The relevant filter object :model:`order.OrderFilter`.

    **Template:**

    :template:`order/Production/all_prodOrders.html`
    """
    filt = OrderFilter(request.GET, Order.objects.filter(order_type="M"))
    prods = ProdTable(filt.qs)
    RequestConfig(request).configure(prods)
    return render(request, 'order/Production/all_prodOrders.html', {'production': prods, 'filter': filt})


def all_prodlines(request):
    """
    Display all :model:`order.OrderLine` of type Production.

    ``prodlines``
        A query set of :model:`order.OrderLine`.

    **Template:**

    :template:`order/Production/all_prodLines.html`
    """
    prodliness = ProdLineTable(OrderLine.objects.filter(order_number__order_type="M"))
    RequestConfig(request).configure(prodliness)
    return render(request, 'order/Production/all_prodLines.html', {'prodlines': prodliness})


def prod_delete(request, order_number):
    """
    Delete an object :model:`order.Order` of type Production.

    ``production``
        A query set of :model:`order.Order`.

    ``filter``
        The relevant filter object :model:`order.OrderFilter`.

    **Template:**

    :template:`order/Production/all_prodOrders.html`
    """
    storage = messages.get_messages(request)
    storage.used = True
    delorder = Order.objects.get(order_number=order_number)

    if delorder.order_status == "C":
        delorder.delete()
    else:
        messages.error(request, "Cannot delete confirmed or invoiced orders", extra_tags='email')

    filt = OrderFilter(request.GET, Order.objects.filter(order_type="M"))
    prods = ProdTable(filt.qs)
    RequestConfig(request).configure(prods)
    return render(request, 'order/Production/all_prodOrders.html', {'production': prods, 'filter': filt})


def prodline_delete(request, mid):
    """
    Delete an object :model:`order.OrderLine` from a Production order.

    ``prodlines``
        A query set of :model:`order.OrderLine`.

    **Template:**

    :template:`order/Production/all_prodLines.html`
    """
    storage = messages.get_messages(request)
    storage.used = True
    delline = OrderLine.objects.get(id=mid)

    if delline.order_number.order_status == "C":
        delline.delete()
    else:
        messages.error(request, "Cannot delete lines from a confirmed or invoiced order", extra_tags='email')

    prodliness = ProdLineTable(OrderLine.objects.filter(order_number__order_type="M"))
    RequestConfig(request).configure(prodliness)
    return render(request, 'order/Production/all_prodLines.html', {'prodlines': prodliness})


def prod_new(request):
    """
     Create a new instance of :model:`order.Order` of type Production.

     ``form``
         An instance of :model:`order.OrderForm`.

     **Template:**

     :template:`order/Production/new_prod.html`
     """
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.order_number = Order.get_next_order_number(order)
            order.order_type = 'M'
            order.order_status = "C"
            order.save()
            form = OrderForm()
    else:
        form = OrderForm()
    return render(request, 'order/Production/new_prod.html', {'form': form})


def prod(request, order_number):
    """
    Create a new instance of :model:`order.Order` of type Production.

    ``form_prod``
        An instance of :model:`order.OrderForm`.

    **Template:**

    :template:`order/Production/Prod.html`
    """
    singleprod = Order.objects.get(order_number=order_number, order_type='M')
    form_order = OrderForm(instance=singleprod)
    return render(request, 'order/Production/Prod.html', {'form_prod': form_order})


def prod_edit(request, order_number):
    """
    Edit/Confirm/Invoice an instance of :model:`order.Order` of type Production.

    ``form_prod``
        An instance of :model:`order.OrderForm`.

    ``form_orderline``
        An instance of :model:`order.OrderLineForm`.

    ``prodlines``
        A query set of :model:`order.OrderLine`.

    ``show_line_form``
        A boolean to determine if the line form should be shown.

    **Template:**

    :template:`order/Production/Prod.html`
    """

    show_line_form = False
    storage = messages.get_messages(request)
    storage.used = True

    if request.GET.get('confirm_order'):
        ord = Order.objects.get(order_number=order_number)
        result = confirmorder(ord)

        if result.confirmation_status == "Ordered":
            ord.order_status = "O"
            ord.save()
        else:
            for er in result.confirmation_errors:
                messages.error(request, er, extra_tags='email')

    if request.GET.get('invoice_order'):
        iord = Order.objects.get(order_number=order_number)
        result = invoiceorder(iord)

        if result.confirmation_status == "Invoiced":
            iord.order_status = "I"
            iord.invoice_date = time.strftime("%Y-%m-%dT%H:%M:%S")
            iord.save()
        else:
            for er in result.confirmation_errors:
                messages.error(request, er, extra_tags='email')

    if request.GET.get('add_line'):
        aord = Order.objects.get(order_number=order_number)
        if aord.order_status == "C":
            show_line_form = True
        else:
            messages.error(request, "Cannot add lines to confirmed or invoiced orders", extra_tags='email')

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
            prodlines = OrderLine.objects.filter(order_number=singleprod)
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

    return render(request, 'order/Production/Prod.html', {'form_prod': form_order, 'form_orderline': form_orderlines,
                                                          'prodlines': prodlines, 'show_line_form': show_line_form})


# Discount views
def setup(request):
    """
    Display the Setup menu.

    **Template:**

    :template:`order/orderSetup.html`
    """
    return render(request, 'order/orderSetup.html')


def all_discounts(request):
    """
    Display all :model:`order.Discounts`.

    ``discounts``
        A query set of :model:`order.Discounts`.

    ``filter``
        The relevant filter object :model:`order.DiscountFilter`.

    **Template:**

    :template:`order/all_discounts.html`
    """
    filt = DiscountFilter(request.GET, Discounts.objects.all())
    discs = DiscountTable(filt.qs)
    RequestConfig(request).configure(discs)
    return render(request, 'order/all_discounts.html', {'discounts': discs, 'filter': filt})


def new_discount(request):
    """
     Create a new instance of :model:`order.Discounts`.

     ``form``
         An instance of :model:`order.DiscountForm`.

     **Template:**

     :template:`order/new_discount.html`
     """
    storage = messages.get_messages(request)
    storage.used = True

    if request.method == "POST":
        form = DiscountForm(request.POST)
        if form.is_valid():
            disc = form.save(commit=False)

            if disc.value < 1 and disc.value > 0:
                disc.save()
            else:
                messages.error(request, "Discount not saved, check value is between 0 (0%) and 1 (100%)",
                               extra_tags='email')

            form = DiscountForm()
    else:
        form = DiscountForm()
    return render(request, 'order/new_discount.html', {'form': form})


def discount_delete(request, lineid):
    """
    Delete an object :model:`order.Discounts`.

    ``discounts``
        A query set of :model:`order.Discounts`.

    **Template:**

    :template:`order/all_discounts.html`
    """
    Discounts.objects.get(id=lineid).delete()
    discs = DiscountTable(Discounts.objects.all())
    RequestConfig(request).configure(discs)
    return render(request, 'order/all_discounts.html', {'discounts': discs})


def discount_edit(request, lineid):
    """
    Edit an instance of :model:`order.Discounts`.

    ``discounts``
        An instance of :model:`order.OrderForm`.

    **Template:**

    :template:`order/all_discounts.html`
    """

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


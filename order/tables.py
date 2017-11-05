from django_tables2.utils import A  # alias for Accessor
# from django_tables2 import tables
import django_tables2 as tables
from order.models import Order
from order.models import OrderLine
from order.models import Discounts


class OrderTable(tables.Table):
    edit_link = tables.LinkColumn('sale_edit', args=[A('order_number')],
                                  verbose_name='Edit order', text='Edit', accessor='pk',
                                  attrs={'class': 'edit_link'})
    delete_link = tables.LinkColumn('sale_delete', args=[A('order_number')],
                                    verbose_name='Delete order', text='Delete', accessor='pk',
                                    attrs={'class': 'delete_link'})

    class Meta:
        attrs = {'class': 'tableStyle'}
        model = Order


class OrderLineTable(tables.Table):
    edit_link = tables.LinkColumn('sale_edit', args=[A('order_number.order_number')],
                                  verbose_name='Edit Line', text='Edit', accessor='order_number',
                                  attrs={'class': 'edit_link'})
    delete_link = tables.LinkColumn('salesline_delete', args=[A('pk')],
                                    verbose_name='Delete Line', text='Delete', accessor='pk',
                                    attrs={'class': 'delete_link'})

    class Meta:
        attrs = {'class': 'tableStyle'}
        model = OrderLine


class DiscountTable(tables.Table):
    edit_link = tables.LinkColumn('discount_edit', args=[A('pk')],
                                  verbose_name='Edit Disc', text='Edit', accessor='pk',
                                  attrs={'class': 'edit_disc'})
    delete_link = tables.LinkColumn('discount_delete', args=[A('pk')],
                                    verbose_name='Delete Disc', text='Delete', accessor='pk',
                                    attrs={'class': 'delete_disc'})

    class Meta:
        attrs = {'class': 'tableStyle'}
        model = Discounts

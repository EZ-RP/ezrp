from django_tables2.utils import A  # alias for Accessor
# from django_tables2 import tables
import django_tables2 as tables
from order.models import Order
from order.models import OrderLine
from order.models import Discounts

# Sales custom tables


class SaleTable(tables.Table):
    edit_link = tables.LinkColumn('sale_edit', args=[A('order_number')],
                                  verbose_name='Edit Sale', text='Edit', accessor='pk',
                                  attrs={'class': 'edit_link'})
    delete_link = tables.LinkColumn('sale_delete', args=[A('order_number')],
                                    verbose_name='Delete Sale', text='Delete', accessor='pk',
                                    attrs={'class': 'delete_link'})

    class Meta:
        attrs = {'class': 'tableStyle'}
        model = Order


class SalesLineTable(tables.Table):
    edit_link = tables.LinkColumn('salesline_edit', args=[A('order_number')],
                                  verbose_name='Edit Sale', text='Edit', accessor='order_number',
                                  attrs={'class': 'edit_link'})
    delete_link = tables.LinkColumn('salesline_delete', args=[A('pk')],
                                    verbose_name='Delete Line', text='Delete', accessor='pk',
                                    attrs={'class': 'delete_link'})

    class Meta:
        attrs = {'class': 'tableStyle'}
        model = OrderLine


class DiscountTable(tables.Table):
    edit_link = tables.LinkColumn('disc_edit', args=[A('pk')],
                                  verbose_name='Edit Disc', text='Edit', accessor='pk',
                                  attrs={'class': 'edit_disc'})
    delete_link = tables.LinkColumn('disc_delete', args=[A('pk')],
                                    verbose_name='Delete Disc', text='Delete', accessor='pk',
                                    attrs={'class': 'delete_disc'})

    class Meta:
        attrs = {'class': 'tableStyle'}
        model = Discounts

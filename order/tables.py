from django_tables2.utils import A  # alias for Accessor
# from django_tables2 import tables
import django_tables2 as tables
from order.models import Order

# Sales custom tables


class SaleTable(tables.Table):
    order_number = tables.LinkColumn('sale', args=[A('order_number')]),
    edit_link = tables.LinkColumn('sale_edit', args=[A('order_number')],
                                  verbose_name='Edit Sale', text='Edit', accessor='pk', attrs={'class': 'edit_link'})
    delete_link = tables.LinkColumn('sale_delete', args=[A('order_number')],
                                    verbose_name='Delete Sale',
                                    text='Delete', accessor='pk', attrs={'class': 'delete_link'})

    class Meta:
        attrs = {'class': 'paleblue'}
        model = Order


from django_tables2.utils import A  # alias for Accessor
# from django_tables2 import tables
import django_tables2 as tables
from stock.models import Inventory


# Stock custom tables


class StockTable(tables.Table):
    # edit_link = tables.LinkColumn('stock_edit', args=[A('item_id')],
    #                              verbose_name='Edit Stock', text='Edit', accessor='pk',
    #                              attrs={'class': 'edit_link'})
    delete_link = tables.LinkColumn('stock_delete', args=[A('item_id')],
                                    verbose_name='Delete Stock', text='Delete', accessor='pk',
                                    attrs={'class': 'delete_link'})

    class Meta:
        attrs = {'class': 'tableStyle'}
        model = Inventory


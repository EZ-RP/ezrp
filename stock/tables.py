from django_tables2.utils import A  # alias for Accessor
# from django_tables2 import tables
import django_tables2 as tables
from stock.models import Inventory


# Stock custom tables


class StockTable(tables.Table):
    """
    assignes what is shown on the stock table
    """
    edit_link = tables.LinkColumn('stock_edit', args=[A('pk')],
                                  verbose_name='Edit Stock', text='Edit', accessor='pk',
                                  attrs={'class': 'edit_link'})
    # delete_link = tables.LinkColumn('stock_delete', args=[A('pk')],
    #                                verbose_name='Delete Stock', text='Delete', accessor='pk',
    #                                attrs={'class': 'delete_link'})

    class Meta:
        attrs = {'class': 'tableStyle'}
        fields = ['item_id.item_number', 'item_id.name', 'available_qty', 'reserved_qty', 'ordered_qty']
        model = Inventory


from django_tables2.utils import A
import django_tables2 as tables
from product.models import Item


class ProductTable(tables.Table):

    edit_link = tables.LinkColumn('edit_product', args=[A('id')],
                                  verbose_name='Edit product', text='Edit', accessor='id',
                                  attrs={'class': 'edit_link'})
    """
    delete_link = tables.LinkColumn('delete_product', args=[A('id')],
                                    verbose_name='Delete Address', text='Delete', accessor='id',
                                    attrs={'class': 'delete_link'})
    """
    class Meta:
        model = Item
        attrs = {'class': 'tableStyle'}
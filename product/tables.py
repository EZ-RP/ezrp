import django_tables2 as tables
from product.models import Item


class ProductTable(tables.Table):
    class Meta:
        model = Item
        attrs = {'class': 'tableStyle'}
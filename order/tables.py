from django_tables2.utils import A  # alias for Accessor
from django_tables2 import tables


class SaleTable(tables.Table):
    name = tables.LinkColumn('sale_detail', args=[A('pk')])

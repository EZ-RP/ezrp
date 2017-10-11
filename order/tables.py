from django_tables2.utils import A  # alias for Accessor
from django_tables2 import tables
from order.models import Order


#class SaleTable(tables.Table):
    #order_number = tables.LinkColumn('all_sales', args=[A('pk')])

    #class Meta:
        #model = Order


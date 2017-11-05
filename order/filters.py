import django_filters as df
from order.models import *


class OrderFilter(df.FilterSet):

    class Meta:
        model = Order
        fields = {
            'order_status': ['icontains'],
            'created_date': ['contains'],
            'invoice_date': ['contains'],
        }



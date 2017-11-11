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


class DiscountFilter(df.FilterSet):

    class Meta:
        model = Discounts
        fields = {
            'item_id': ['icontains'],
            'start_date': ['contains'],
            'end_date': ['contains'],
        }


import django_filters as df
from stock.models import Inventory


class StockFilter(df.FilterSet):
    """
    is the code that tells the what fields to filter. icontains makes the search case insensitive
    """
    class Meta:
        model = Inventory
        fields = {
            'item_id__item_number': ['contains'],
            'item_id__name': ['icontains'],
        }



import django_filters as df
from stock.models import Inventory


class StockFilter(df.FilterSet):

    class Meta:
        model = Inventory
        fields = {
            'item_id__item_number': ['contains'],
            'item_id__name': ['contains'],
        }



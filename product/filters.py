import django_filters as df
from product.models import Item


class ProductFilter(df.FilterSet):

    class Meta:
        model = Item
        fields = {
            'item_number': ['contains'],
            'name': ['icontains'],
        }
from django_tables2.utils import A
import django_tables2 as tables
from party.models import Party


class CustomerTable(tables.Table):
    account_number = tables.LinkColumn('customer', args=[A('pk')])

    class Meta:
        model = Party

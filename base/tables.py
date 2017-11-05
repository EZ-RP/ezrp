from django_tables2.utils import A
import django_tables2 as tables
from base.models import *


class PayDetailsTable(tables.Table):

    delete_link = tables.LinkColumn('pay_details_delete', args=[A('pk')],
                                    verbose_name='Delete pay details', text='Delete', accessor='pk',
                                    attrs={'class': 'delete_link'})

    class Meta:
        model = PayDetails
        attrs = {'class': 'tableStyle'}
from django_tables2.utils import A
import django_tables2 as tables
from party.models import *
from base.models import Address


class CustomerTable(tables.Table):

    edit_link = tables.LinkColumn('customer', args=[A('pk')],
                                  verbose_name='Edit Customer', text='Edit', accessor='pk',
                                  attrs={'class': 'edit_link'})

    delete_link = tables.LinkColumn('customer_delete', args=[A('pk')],
                                    verbose_name='Delete Customer', text='Delete', accessor='pk',
                                    attrs={'class': 'delete_link'})

    class Meta:
        model = Party
        attrs = {'class': 'tableStyle'}


class CustomerAddress(tables.Table):

    edit_link = tables.LinkColumn('edit_address', args=[A('id')],
                                  verbose_name='Edit Address', text='Edit', accessor='id',
                                  attrs={'class': 'edit_link'})

    delete_link = tables.LinkColumn('delete_address', args=[A('id')],
                                    verbose_name='Delete Address', text='Delete', accessor='id',
                                    attrs={'class': 'delete_link'})


    class Meta:
        model = PartyAddress
        fields = ['address_id.street', 'address_id.suburb', 'address_id.state', 'address_id.postcode']
        attrs = {'class': 'tableStyle'}

from django.db import models
from base.models import Address

"""Naming conventions:
    - Class names                           = CamelCase
    - Function or model field names         = lowercase_underscore"""


class Party(models.Model):
    PARTY_TYPE = (
        ('C', 'Customer'),
        ('V', 'Vendor'),
    )

    account_number = models.CharField(max_length=10, primary_key=1)
    business_number = models.CharField(max_length=20)
    party_name = models.CharField(max_length=100)
    party_type = models.CharField(max_length=1, choices=PARTY_TYPE)

    def __str__(self):
        return '%s %s' % (self.account_number, self.party_name)

class PartyAddress(models.Model):

    account_number = models.ForeignKey(Party, on_delete=models.CASCADE, verbose_name='Related account')
    address_id = models.ForeignKey(Address, verbose_name='Related address')

    def add_address_ref(self, address: Address, party: Party):
        self.account_number = party
        self.address_id = address
        self.save()


from django.db import models
from base.models import Address


class Party(models.Model):
    """
    Stores a single party entry
    """

    PARTY_TYPE = (
        ('C', 'Customer'),
        ('V', 'Vendor'),
    )

    account_number = models.CharField(max_length=10,
                                      primary_key=1,
                                      help_text="The unique account number of the party")

    business_number = models.CharField(max_length=20,
                                       help_text="The formal business number of the party")

    party_name = models.CharField(max_length=100,
                                  help_text="Party name")

    party_type = models.CharField(max_length=1,
                                  choices=PARTY_TYPE,
                                  help_text="The type of the party - Customer or vendor")

    def __str__(self):
        return '%s %s' % (self.account_number, self.party_name)

class PartyAddress(models.Model):
    """
    Stores address linked to a party, related to :model:'party.Party'
    and :model:'base.Address'.
    """
    account_number = models.ForeignKey(Party, on_delete=models.CASCADE, verbose_name='Related account')
    address_id = models.ForeignKey(Address, verbose_name='Related address')

    def add_address_ref(self, address: Address, party: Party):
        self.account_number = party
        self.address_id = address
        self.save()


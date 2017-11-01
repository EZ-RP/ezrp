import django_filters as df
from party.models import Party


class PartyFilter(df.FilterSet):

    class Meta:
        model = Party
        fields = {
            'account_number': ['contains'],
            'party_name': ['contains'],
        }



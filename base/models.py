from django.db import models


"""Naming conventions:
    - Class names                           = CamelCase
    - Function or model field names         = lowercase_underscore"""


class Address(models.Model):
    """
    The base address table which stores addresses irrelevant of there significance
    """
    street = models.CharField(max_length=150, help_text="The street and relevant street numbers")
    suburb = models.CharField(max_length=150, help_text="Suburb the street is located in")
    state = models.CharField(max_length=150, help_text="the state the suburb is located in")
    postcode = models.CharField(max_length=10, help_text="the postcode related to the suburb")
    country = models.CharField(max_length=50, default="Australia", help_text="the country the address belongs to")

    def __str__(self):
        """
        The display of an address record in a related table
        """
        return '%s %s %s %s' % (self.street, self.suburb, self.state, self.postcode)


class PayDetails(models.Model):
    """
    The Payment details for the Specified Account
    """
    account_number = models.CharField(max_length=10, help_text="Account the pay details belong to")
    bsb_number = models.CharField(max_length=10, help_text="Bank State Branch or Bank code")
    account_name = models.CharField(max_length=20, help_text="Name the Bank Account is under")


# DS: SystemParameters Table
class SystemParameters (models.Model):
    """
    Stores Parameters that can be used anywhere throughout the system
    """
    description = models.CharField(max_length=200, help_text="description or name of the parameter")
    str_value = models.CharField(max_length=150, help_text="value of the parameter")



from django.db import models


class ConfirmResult:
    """
    The result object of a confirmation or invoice
    """
    def __init__(self):
        """
        The initialisation of the object
        """
        self.confirmation_status = ''
        self.confirmation_errors = []

    def add_error(self, error: str):
        """
        Adds an error to confirmation_errors
        """
        self.confirmation_errors.append(error)

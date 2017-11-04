from django.db import models


class ConfirmResult:
    def __init__(self):
        self.confirmation_status = ''
        self.confirmation_errors = []

    def add_error(self, error: str):
        self.confirmation_errors.append(error)

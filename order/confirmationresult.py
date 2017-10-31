from django.db import models


class FileInfo(object):
    def __init__(self, file):
        self.url = file.url # do whatever
        self.title = file.title # do whatever
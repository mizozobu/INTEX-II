from django.db import models
from cuser.models import AbstractCUser


class User(AbstractCUser):
    birthdate = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    zip = models.TextField(blank=True, null=True)

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

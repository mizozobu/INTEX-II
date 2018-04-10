from django.db import models
from cuser.models import AbstractCUser
from catalog import models as cmod


class User(AbstractCUser):
    birthdate = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    zip = models.TextField(blank=True, null=True)

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_shopping_cart(self):
        order = cmod.Order.objects.all()
        order = order.filter(user=User.objects.get(email=self.email)).filter(status="cart").first()
        if order is None:
            print("New Order Created")
            o = cmod.Order()
            o.status = "cart"
            o.user = self
            o.save()
            return o
        else:
            print("Order not created")
            return order

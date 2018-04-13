from django_mako_plus import view_function
from catalog import models as cmod
from django.http import HttpResponseRedirect


@view_function
def process_request(request, orderItem: cmod.OrderItem, order: cmod.Order):
    orderItem.status = 'deleted'
    orderItem.save()
    order.recalculate()

    return HttpResponseRedirect('/catalog/cart/' + str(order.id))

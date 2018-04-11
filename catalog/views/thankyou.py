from django_mako_plus import view_function, jscontext
from catalog import models as cmod
from django.conf import settings


@view_function
def process_request(request, orderid):

    orderid = int(orderid)

    order = cmod.Order.objects.get(id=orderid)

    items = order.active_items(False)

    tax = order.get_item(cmod.Product.objects.get(name="Sales Tax"))

    for i in items:
        i.recalculate()
    order.recalculate()

    context = {
        'order': order,
        'items': items,
        'tax': tax,
    }

    return request.dmp.render('thankyou.html', context)

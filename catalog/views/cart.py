from django_mako_plus import view_function, jscontext
from catalog import models as cmod
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import redirect


@view_function
def process_request(request, order: cmod.Order=None):
    if order is not None:
        HttpResponseRedirect('/homepage/')
        items = order.active_items(False)
        tax = order.get_item(cmod.Product.objects.get(name="Sales Tax"))
        for i in items:
            i.recalculate()
        order.recalculate()

        if order.num_items() < 2:
            HttpResponseRedirect('/catalog/')

        context = {
            'items': items,
            'order': order,
            'tax': tax
        }

        return request.dmp.render('cart.html', context)
    else:
        return HttpResponseRedirect('/index/')

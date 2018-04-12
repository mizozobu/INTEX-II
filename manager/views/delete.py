from django_mako_plus import view_function
from catalog import models as m
from django.http import HttpResponseRedirect


@view_function
def process_request(request, p: m.Product):
    if request.user.is_superuser:
        p.status = 2
        p.save()
        return HttpResponseRedirect('/manager/')
    else:
        return HttpResponseRedirect('/index/')

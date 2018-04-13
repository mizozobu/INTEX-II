from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
import random


@view_function
def process_request(request, counter):
    counter = 0
    context = {
        'now': datetime.now().strftime('%H:%M:%S'),
        'st': counter,
    }
    if request.urlparams[0] == 'gettime':
        counter += 1
        return request.dmp.render('ajax.html', context, def_name='server_time')
    return request.dmp.render('ajax.html', context)

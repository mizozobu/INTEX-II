from django_mako_plus import view_function, jscontext
from catalog import models as cmod
from django.conf import settings


@view_function
def process_request(request):
    context = {
    }

    return request.dmp.render('thankyou.html', context)

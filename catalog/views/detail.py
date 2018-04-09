from django_mako_plus import view_function
from catalog import models as m


@view_function
def process_request(request, product: m.Product=None):
    context = {
        'product': product,
    }
    return request.dmp.render('detail.html', context)

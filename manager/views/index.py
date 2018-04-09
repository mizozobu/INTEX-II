from django_mako_plus import view_function
from catalog import models as m

@view_function
def process_request(request):
    products = m.Product.objects.all()
    context = {
        'products': products,
    }
    return request.dmp.render('index.html', context)

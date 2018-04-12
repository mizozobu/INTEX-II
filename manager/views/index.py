from django_mako_plus import view_function
from catalog import models as m

@view_function
def process_request(request):
    products = m.Product.objects.all()

    bulkproducts = m.BulkProduct.objects.all()

    lowProducts = []

    for item in bulkproducts:
        if item.quantity <= item.order_trigger:
            lowProducts.append(item)

    context = {
        'products': products,
        'lowProducts': lowProducts,
    }

    return request.dmp.render('index.html', context)

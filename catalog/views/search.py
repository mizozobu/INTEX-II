from django_mako_plus import view_function
from catalog import models as m
from django.http import JsonResponse


@view_function
def process_request(request):
    products = m.Product.objects.all()

    # name
    name = request.GET.get('name', None)
    if name is not None:
        products = products.filter(name__icontains=name)

    # max price
    max_price = request.GET.get('max_price', 999999)
    products = products.filter(price__lt=max_price)

    # category
    category = request.GET.get('category', None)
    if category is not None:
        products = products.filter(category__name__icontains=category)

    # page
    page = request.GET.get('page', 1)
    products = products[(page-1)*6:page*6]

    products = list(products.values('category__name', 'name', 'price'))
    return JsonResponse({ "products": products })

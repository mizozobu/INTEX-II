from django_mako_plus import view_function, jscontext
from catalog import models as m
import math


@view_function
def process_request(request, category: m.Category=None, page: int=1):
    products = m.Product.objects.all()
    category_name = "All Products"
    category_id = 0
    if category is not None:
        products = products.filter(category=category)
        category_name = category.name
        category_id = category.id

    # total page number
    num_pages = math.ceil(products.count()/6)
    products = products[(page-1)*6:page*6]

    categories = m.Category.objects.all()
    category_ids = []
    for c in categories:
        category_ids.append(str(c.id))
    context = {
        'products': products,
        'categories': categories,
        'category_id': category_id,
        'category_ids': category_ids,
        'category_name': category_name,
        'num_pages': num_pages,
        'page': page,
        jscontext('category_id_js'): category_id,
    }
    return request.dmp.render('index.html', context)


@view_function
def products(request, category: m.Category=None, page: int=1):
    products = m.Product.objects.all()
    category_name = "All Products"
    category_id = 0
    if category is not None:
        products = products.filter(category=category)
        category_name = category.name
        category_id = category.id

    # total page number
    num_pages = math.ceil(products.count()/6)
    products = products[(page-1)*6:page*6]

    categories = m.Category.objects.all()
    category_ids = []
    for c in categories:
        category_ids.append(str(c.id))
    context = {
        'products': products,
        'categories': categories,
        'category_id': category_id,
        'category_ids': category_ids,
        'category_name': category_name,
        'num_pages': num_pages,
        'page': page,
        jscontext('category_id_js'): category_id,
    }
    return request.dmp.render('index.products.html', context)

from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod
import re

@view_function
def process_request(request):

#graph for revenue of categories sold
    allCategories= cmod.Category.objects.all()
    allOrders= cmod.Order.objects.all()
    allOrderItems=cmod.OrderItem.objects.all()
    allPaymentItems=cmod.Payment.objects.all()
    allProducts=cmod.Product.objects.all()


    a={}
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxyyyy")
    for x in allOrderItems:
        # print(x.product.category.name)
        # print(x.extended)
        # print(a.get(x.product.category.name))
        print("ooooooasdfasdfasdf",x.extended)
        if x.product.category.name in a:
            amount = a.get(x.product.category.name)+x.extended
            a[x.product.category.name]=amount
            print(amount, "amountamountamountamountamountamountamount")
            print(a.get(x.product.category.name),"aaaaaaaaaaaaaaaaaaaaaaaaaa")
        else:
            a[x.product.category.name]=x.extended

    for z in a:
        print(z, a.get(z))
        # if x.product.category.name in [cata[0] for cata in a ]:
        #     # a[x.product.category]+=x.extend
        #     print(a.index([product.category.name, r"\d"]))
        #     # someohow find the array for right category and add x.extend to cata[1]
        # else:
        #     # if not exist in a, add cata as new category
        #     a{x.product.category.name}
        #     a.append([x.product.category.name,  x.extended])
        #     print("xzxxxxxxxxxxxxxxxxxxxxxxxx", x.product.category.name)


    categoryRevenue=[]
    for b in allCategories:
        if b.name not in a:
            a[b.name]=0
        else:
            categoryRevenue.append([b.name, a.get(b.name)])
    print(categoryRevenue)
    context = {
        'catRev':categoryRevenue,


    }

    return request.dmp.render('dashboard.html', context)

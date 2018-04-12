from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod
import re
import calendar

@view_function
def process_request(request):

#graph for revenue of categories sold
    allCategories= cmod.Category.objects.all()
    allOrders= cmod.Order.objects.all()
    allOrderItems=cmod.OrderItem.objects.all()
    allPaymentItems=cmod.Payment.objects.all()
    allProducts=cmod.Product.objects.all()

#line graph
    dateRevDict={}
    for q in allPaymentItems:
        if calendar.month_abbr[q.payment_date.month] in dateRevDict:
            amount = dateRevDict.get(calendar.month_abbr[q.payment_date.month])+float(q.amount)
            dateRevDict[str(calendar.month_abbr[q.payment_date.month])]=float(amount)
        else:
            dateRevDict[str(calendar.month_abbr[q.payment_date.month])]=float(q.amount)

        print("aaaaaaaaaaaaaaaaaaa", dateRevDict)

    categoryRevenue=['Month', 'Revenue']
    print(categoryRevenue)
    for t in range(1,13):
        print(t)
        if calendar.month_abbr[t] not in dateRevDict:
            dateRevDict[str(calendar.month_abbr[q.payment_date.month])]=0

        # categoryRevenue.append([calendar.month_abbr[t], dateRevDict[calendar.month_abbr[t]]])

    for m in categoryRevenue:
        print("vvvvvvvvvvvvvvvv",categoryRevenue)
        # if t.name not in a:
        #     a[t.name]=0
        # decVal=t.get(t.name)
        #
        # categoryRevenue.append([t.name,float(decVal)])



#end of line graph

#pie graph

    a={}

    for x in allOrderItems:

        if x.product.category.name in a:
            amount = a.get(x.product.category.name)+x.extended
            a[x.product.category.name]=amount
        else:
            a[x.product.category.name]=x.extended

    categoryRevenue=[]
    for b in allCategories:
        if b.name not in a:
            a[b.name]=0
        decVal=a.get(b.name)

        categoryRevenue.append([b.name,float(decVal)])
#end of pie graph



    context = {
        'catRev':categoryRevenue,


    }

    return request.dmp.render('dashboard.html', context)

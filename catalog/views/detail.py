from django_mako_plus import view_function
from catalog import models as m
from account import models as a
from django import forms
from formlib.form import Formless


@view_function
def process_request(request, product: m.Product=None):
    print("!!!!!!!!!!!!!!!!", product)
    form = BuyNowForm(request)
    if form.is_valid():
        form.commit(product)
    print("Plzzzzzzzzzzzzzzzzzzz worklkkkkkkkkkkkkkkkkkkkkkkkkkk")
    context = {
        'product': product,
        'form': form,
    }
    return request.dmp.render('detail.html', context)


class BuyNowForm(Formless):
    def init(self):
        self.fields['quantity'] = forms.IntegerField(label='Quantity', initial="1")
        self.fields['quantity'].widget.attrs = {'class': 'quantity'}
        self.user = None

    def clean(self):
        self.user = self.request.user
        print("Yoooooooooooooooooo dawgggggggggggggg")
        if not self.user.is_authenticated:
            raise forms.ValidationError("Log in to add items to your cart!")
        return self.cleaned_data

    def commit(self, product):
        print("HILARYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
        u = a.User.objects.get(email=self.request.user)
        o = u.get_shopping_cart()
        print("OOOOOOOOOOOORDERRRRRRR", o)
        q = self.cleaned_data.get('quantity')
        taxProd = m.Product.objects.get(name="Sales Tax")
        if o.active_items:
            prodExists = False
            for i in o.active_items(False):
                if i.product.id == product.id:
                    i.quantity += int(q)
                    i.save()
                    i.recalculate()
                    prodExists = True
            if prodExists is False:
                li = o.get_item(product, True)
                li.quantity = int(q)
                li.save()
                li.recalculate()
            hasTax = False
            if taxProd in o.active_items():
                hasTax = True
            if hasTax is False:
                tx = o.get_item(taxProd, True)
                tx.save()
        o.recalculate()

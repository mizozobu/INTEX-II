# from django_mako_plus import view_function
# from catalog import models as m
#
#
# @view_function
# def process_request(request, product: m.Product=None):
#     context = {
#         'product': product,
#     }
#     return request.dmp.render('checkout.html', context)
from django_mako_plus import view_function
from catalog import models as cmod
from formlib.form import Formless
from django import forms
from django.http import HttpResponseRedirect


@view_function
def process_request(request, order: cmod.Order):
    form = CheckoutForm(request)
    form.submit_text = None
    if form.is_valid():
        form.commit()
        return HttpResponseRedirect('/catalog/thankyou')
    context = {
        'form': form,
        'order': order
    }

    return request.dmp.render('checkout.html', context)


class CheckoutForm(Formless):
    def init(self):
        self.fields['address1'] = forms.CharField(label="Address 1", required=False)
        self.fields['address2'] = forms.CharField(label="Address 2", required=False)
        self.fields['city'] = forms.CharField(label="City", required=False)
        self.fields['state'] = forms.CharField(label="State", required=False)
        self.fields['zip'] = forms.CharField(label="Zip Code", required=False)
        self.fields['stripeToken'] = forms.CharField(label="stripeToken", widget=forms.HiddenInput())

    def clean(self):
        o = cmod.Order.objects.all()
        o = o.filter(user=self.request.user).filter(status="cart").first()
        for i in o.active_items(False):
            if i.quantity > i.product.quantity:
                raise forms.ValidationError("We only have " + str(i.product.quantity) + " of " + i.product.name + " left!")
            elif i.product.status == "I":
                raise forms.ValidationError("The " + i.product.name + " product is no longer available.")
        try:
            o.finalize(self.cleaned_data.get('stripeToken'))
        except ValueError:
            raise forms.ValidationError("There was an error charging your account!")
        return self.cleaned_data

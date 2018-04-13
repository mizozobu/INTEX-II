from django_mako_plus import view_function
from django import forms
from django.http import HttpResponseRedirect
from formlib.form import Formless
from catalog import models as m
from django.forms.widgets import SelectDateWidget


@view_function
def process_request(request, p: m.Product=None):
    if request.user.is_superuser:
        if request.method == 'GET':
            if type(p) is m.BulkProduct:
                t = "1"
            elif type(p) is m.IndividualProduct:
                t = "2"
            elif type(p) is m.RentalProduct:
                t = "3"

            form = ProductForm(request, initial={
                'id': p.id,
                'type': t,
                'name': p.name,
                'price': p.price,
                'status': 'Active' if p.status == '1' else 'Inactive',
                'description': p.description,
                'category': p.category.name,
                # unique fields
                'unit': p.unit if type(p) is m.BulkProduct else None,
                'order_trigger': p.order_trigger if type(p) is m.BulkProduct else None,
                'order_quantity': p.order_quantity if type(p) is m.BulkProduct else None,
                'rental_period': p.rental_period if type(p) is m.RentalProduct else None,
                'retire_date': p.retire_date if type(p) is m.RentalProduct else None,
                })
        elif request.method == 'POST':
            form = ProductForm(request)

        if form.is_valid():
            p = m.Product.objects.get(id=int(request.dmp.urlparams[0]))
            p.name = form.cleaned_data.get('name')
            p.price = form.cleaned_data.get('price')
            p.status = form.cleaned_data.get('status')
            p.description = form.cleaned_data.get('description')
            p.category = form.cleaned_data.get('category')

            if form.cleaned_data.get('type') == '1':
                p.unit = form.cleaned_data.get('unit')
                p.order_trigger = form.cleaned_data.get('order_trigger')
                p.order_quantity = form.cleaned_data.get('order_quantity')
            if form.cleaned_data.get('type') == '2':
                pass
            if form.cleaned_data.get('type') == '3':
                p.rental_period = form.cleaned_data.get('rental_period')
                p.retire_date = form.cleaned_data.get('retire_date')

            p.save()
            return HttpResponseRedirect('/manager/')

        context = {
            'form': form,
            'id': p.id
        }

        return request.dmp.render('edit.html', context)
    else:
        return HttpResponseRedirect('/index/')


class ProductForm(Formless):
    def init(self):
        types = (
            (1, "Bulk Product"),
            (2, "Individual Product"),
            (3, "Rental Product"),
        )
        statuses = (
            (1, "Active"),
            (2, "Inactive"),
        )
        self.fields['id'] = forms.IntegerField(label="", widget=forms.TextInput(attrs={'class': 'd-none'}))
        self.fields['type'] = forms.ChoiceField(label="", choices=types, widget=forms.TextInput(attrs={'class': 'd-none'}))
        self.fields['name'] = forms.CharField(label="Name")
        self.fields['price'] = forms.CharField(label="Price")
        self.fields['status'] = forms.ChoiceField(label="Status", choices=statuses)
        self.fields['description'] = forms.CharField(label="Description")
        self.fields['category'] = forms.ModelChoiceField(label="Category", queryset=m.Category.objects.all(), empty_label=None)

        # bulk
        self.fields['unit'] = forms.CharField(label="Unit", required=False, widget=forms.TextInput(attrs={'class': 'bulk'}))
        self.fields['order_trigger'] = forms.DecimalField(label="Order Trigger", required=False, widget=forms.TextInput(attrs={'class': 'bulk'}))
        self.fields['order_quantity'] = forms.DecimalField(label="Order Quantity", required=False, widget=forms.TextInput(attrs={'class': 'bulk'}))

        # nothing for Individual

        # rental
        self.fields['rental_period'] = forms.IntegerField(label="Rental Period", required=False, widget=forms.TextInput(attrs={'class': 'rental'}))
        self.fields['retire_date'] = forms.DateField(label="Retire Date", required=False, widget=forms.TextInput(attrs={'class': 'rental'}))

    def clean(self):
        if self.cleaned_data.get('type') == '1':
            if self.cleaned_data.get('unit') == '':
                raise forms.ValidationError('Unit is required.')
            if self.cleaned_data.get('order_trigger') == '':
                raise forms.ValidationError('Order Trigger is required.')
            if self.cleaned_data.get('order_quantity') == '':
                raise forms.ValidationError('Order Quantity is required.')
        if self.cleaned_data.get('type') == '2':
            pass
        if self.cleaned_data.get('type') == '3':
            if self.cleaned_data.get('rental_period') == '':
                raise forms.ValidationError('Rental Period is required.')
            if self.cleaned_data.get('retire_date') == '':
                raise forms.ValidationError('Retire Date is required.')
        return self.cleaned_data

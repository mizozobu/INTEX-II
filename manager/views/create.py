from django_mako_plus import view_function
from django import forms
from django.http import HttpResponseRedirect
from formlib.form import Formless
from catalog import models as m
from django.forms.widgets import SelectDateWidget


@view_function
def process_request(request, p: m.Product=None):
    form = ProductForm(request)
    if form.is_valid():
        form.commit()
        return HttpResponseRedirect('/manager/')

    context = {
        'form': form,
    }
    return request.dmp.render('create.html', context)


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
        self.fields['type'] = forms.ChoiceField(label="Type", choices=types, initial='2')
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

    def clean_type(self):
        type = self.cleaned_data.get('type')
        if type == '':
            raise forms.ValidationError("Type is required.")
        return type

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

    def commit(self):
        # unique fields
        if self.cleaned_data.get('type') == '1':
            p = m.BulkProduct()
            p.unit = self.cleaned_data.get('unit')
            p.order_trigger = self.cleaned_data.get('order_trigger')
            p.order_quantity = self.cleaned_data.get('order_quantity')
        if self.cleaned_data.get('type') == '2':
            p = m.IndividualProduct()
        if self.cleaned_data.get('type') == '3':
            p = m.RentalProduct()
            p.rental_period = self.cleaned_data.get('rental_period')
            p.retire_date = self.cleaned_data.get('retire_date')
        p.name = self.cleaned_data.get('name')
        p.price = self.cleaned_data.get('price')
        p.status = self.cleaned_data.get('status')
        p.description = self.cleaned_data.get('description')
        p.category = self.cleaned_data.get('category')

        p.save()

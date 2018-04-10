from django.db import models, transaction
from django.conf import settings
from django.forms.models import model_to_dict
from polymorphic.models import PolymorphicModel
from decimal import Decimal
from datetime import datetime
import stripe


class Order(models.Model):
    '''An order in the system'''
    STATUS_CHOICES = (
        ('cart', 'Shopping Cart'),
        ('payment', 'Payment Processing'),
        ('sold', 'Finalized Sale'),
    )
    order_date = models.DateTimeField(null=True, blank=True)
    name = models.TextField(blank=True, default="Shopping Cart")
    status = models.TextField(choices=STATUS_CHOICES, default='cart', db_index=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)  # max number is 999,999.99
    user = models.ForeignKey('account.User', related_name='orders',  on_delete=models.CASCADE)
    # shipping information
    ship_date = models.DateTimeField(null=True, blank=True)
    ship_tracking = models.TextField(null=True, blank=True)
    ship_name = models.TextField(null=True, blank=True)
    ship_address = models.TextField(null=True, blank=True)
    ship_city = models.TextField(null=True, blank=True)
    ship_state = models.TextField(null=True, blank=True)
    ship_zip_code = models.TextField(null=True, blank=True)

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Order {}: {}: {}'.format(self.id, self.user.get_full_name(), self.total_price)

    def active_items(self, include_tax_item=True):
        '''Returns the active items on this order'''
        items = self.items.all()
        items = items.filter(status="active")
        if include_tax_item is False:
            items = items.exclude(product=Product.objects.get(name="Sales Tax"))
        return items

    def get_item(self, product, create=False):
        '''Returns the OrderItem object for the given product'''
        item = OrderItem.objects.filter(order=self, product=product).first()
        if item is None and create:
            item = OrderItem.objects.create(order=self, product=product, price=product.price, quantity=0)
        elif create and item.status != 'active':
            item.status = 'active'
            item.quantity = 0
        if item is not None:
            item.recalculate()
            item.save()
        item.recalculate()
        item.save()
        return item

    def num_items(self):
        '''Returns the number of items in the cart'''
        return sum(self.active_items(include_tax_item=False).values_list('quantity', flat=True))

    def recalculate(self):
        '''
        Recalculates the total price of the order,
        including recalculating the taxable amount.

        Saves this Order and all child OrderLine objects.
        '''
        total = 0
        for i in self.active_items(False):
                i.recalculate()
                total += i.extended

        tax = (float(total) * float(.07))
        finTotal = float(total) + float(tax)
        self.total_price = round(finTotal, 2)
        salesTax = self.get_item(Product.objects.get(name="Sales Tax"))
        salesTax.price = tax
        salesTax.save()
        salesTax.recalculate()
        self.save()

    def finalize(self, stripe_charge_token):
        '''Runs the payment and finalizes the sale'''
        with transaction.atomic():
            for i in self.active_items(True):
                i.recalculate()
                p = i.product
                if p.__class__.__name__ == "BulkProduct":
                    p.quantity = p.quantity - i.quantity
                    p.save()
                else:
                    if p.name != "Sales Tax":
                        p.status = 'I'
                        p.save()
            self.recalculate()
            stripe.Charge.create(
                amount=int(self.total_price * 100),
                currency="usd",
                description="FOMO Product Charge",
                source=stripe_charge_token
            )
            payment = Payment(order=self, amount=self.total_price, validation_code=stripe_charge_token)
            payment.save()
            self.status = "sold"
            self.save()


class OrderItem(PolymorphicModel):
    '''A line item on an order'''
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('deleted', 'Deleted'),
    )
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    status = models.TextField(choices=STATUS_CHOICES, default='active', db_index=True)
    product = models.ForeignKey('Product', null=True, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)  # max number is 999,999.99
    quantity = models.IntegerField(default=0)
    extended = models.DecimalField(max_digits=8, decimal_places=2, default=0)  # max number is 999,999.99

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'OrderItem {}: {}: {}'.format(self.id, self.product.name, self.extended)

    def recalculate(self):
        '''Updates the order item's price, quantity, extended'''
        p = Product.objects.get(id=self.product.id)
        if p.name != "Sales Tax":
            self.price = p.price
            if self.quantity == 0:
                self.quantity = 1
            self.extended = (self.price * self.quantity)
            self.save()
        else:
            self.extended = self.price
            self.save()


class Payment(models.Model):
    '''A payment on a sale'''
    order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(null=True, blank=True, auto_now=True)
    amount = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2)  # max number is 999,999.99
    validation_code = models.TextField(null=True, blank=True)


class Category(models.Model):
    name = models.TextField()
    description = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        print("-----------------------------------stringfy")
        return self.name


class Product(PolymorphicModel):
    '''polymorphic super class'''
    statuses = (
        (1, "Active"),
        (2, "Inactive"),
    )

    name = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.TextField(choices=statuses, default=1)
    description = models.TextField()
    quantity = models.DecimalField(
        max_digits=6, decimal_places=2, default=1.00)
    create_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    # FK to Category
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def image_url(self):
        filename = 'image_unavailable.gif'
        if self.images.all().first():
            filename = self.images.all().first().filename
        return '{}catalog/media/products/{}'.format(settings.STATIC_URL, filename)

    def image_urls(self):
        if self.images.all():
            image_list = []
            for image in self.images.all():
                image_list.append(
                    '{}catalog/media/products/{}'.format(settings.STATIC_URL, image.filename))
            return image_list
        else:
            return ['{}catalog/media/products/{}'.format(settings.STATIC_URL, 'image_unavailable.gif')]


class BulkProduct(Product):
    '''bulk product'''
    unit = models.TextField()
    order_trigger = models.DecimalField(max_digits=6, decimal_places=2)
    order_quantity = models.DecimalField(max_digits=6, decimal_places=2)


class IndividualProduct(Product):
    '''individual product'''
    product_id = models.TextField(primary_key=True)


class RentalProduct(Product):
    '''rental product'''
    product_id = models.TextField(primary_key=True)
    rental_period = models.IntegerField()
    retire_date = models.DateField()


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE)
    filename = models.TextField(default="image_unavailable")

#######################################################################
# Products
# various product models go here
#######################################################################
# Orders


# class Order(models.Model):
#     '''An order in the system'''
#     STATUS_CHOICES = (
#         ('cart', 'Shopping Cart'),
#         ('payment', 'Payment Processing'),
#         ('sold', 'Finalized Sale'),
#     )
#     order_date = models.DateTimeField(null=True, blank=True)  # maybe auto_add?
#     name = models.TextField(blank=True, default="Shopping Cart")  # ?
#     status = models.TextField(choices=STATUS_CHOICES,
#                               default='cart', db_index=True)
#     total_price = models.DecimalField(
#         max_digits=8, decimal_places=2, default=0)  # max number is 999,999.99
#     user = models.ForeignKey('account.User', related_name='orders',
#                              on_delete=models.CASCADE)  # '' not needed?
#     # shipping information
#     ship_date = models.DateTimeField(null=True, blank=True)
#     ship_tracking = models.TextField(null=True, blank=True)
#     ship_name = models.TextField(null=True, blank=True)
#     ship_address = models.TextField(null=True, blank=True)
#     ship_city = models.TextField(null=True, blank=True)
#     ship_state = models.TextField(null=True, blank=True)
#     ship_zip_code = models.TextField(null=True, blank=True)
#
#     def __str__(self):
#         '''Prints for debugging purposes'''
#         return 'Order {}: {}: {}'.format(self.id, self.user.get_full_name(), self.total_price)
#
#     def active_items(self, include_tax_item=True):
#         '''Returns the active items on this order'''
#         # create a query object (filter to status='active')
#         orderItems = OrderItem.objects.filter(status='active')
#         if include_tax_item:
#             # is the name right?
#             return orderItems
#         else:
#             # is the name right?
#             return orderItems.exclude(product=Product.objects.get(name='Sales Tax').id)
#         # if we aren't including the tax item, alter the
#         # query to exclude that OrderItem
#         # I simply used the product name (not a great choice,
#         # but it is acceptable for credit)
#
#     def get_item(self, product, create=False):
#         '''Returns the OrderItem object for the given product'''
#         item = OrderItem.objects.filter(order=self, product=product).first()
#         if item is None and create:
#             item = OrderItem.objects.create(
#                 order=self, product=product, price=product.price, quantity=0)
#         elif create and item.status != 'active':
#             item.status = 'active'
#             item.quantity = 0
#         if item is not None:
#             item.recalculate()
#             item.save()
#         item.recalculate()
#         item.save()
#         return item
#
#     def num_items(self):
#         '''Returns the number of items in the cart'''
#         return sum(self.active_items(include_tax_item=False).values_list('quantity', flat=True))
#
#     def recalculate(self):
#         '''
#         Recalculates the total price of the order,
#         including recalculating the taxable amount.
#
#         Saves this Order and all child OrderLine objects.
#         '''
#         # iterate the order items (not including tax item) and get the total price
#         # call recalculate on each item
#         self.total_price = 0
#         for order_item in self.active_items(include_tax_item=False):
#             order_item.recalculate()
#             self.total_price += order_item.extended
#
#         # update/create the tax order item (calculate at 7% rate)
#         order_items = OrderItem.objects.filter(order=self)
#         sales_tax = order_items.Product.get(name='sales tax')
#         sales_tax.price = self.total_price * 0.07
#         sales_tax.save()
#         # update the total and save
#         self.total_price += sales_tax
#         self.save()
#
#     def finalize(self, stripe_charge_token):
#         '''Runs the payment and finalizes the sale'''
#         with transaction.atomic():
#             # recalculate just to be sure everything is updated
#             for order_item in self.active_items(include_tax_item=False):
#                 order_item.recalculate()
#                 # check that all products are available
#                 if order_item.Product.quantity < order_item.quantity:
#                     raise Exception('{} is not available'.format(
#                         order_item.Product.name))
#
#             # contact stripe and run the payment (using the stripe_charge_token)
#
#             # finalize (or create) one or more payment objects
#             payment = Payment()
#             payment.order = self
#             payment.payment_date = datetime.now()
#             payment.amount = self.total_price
#             payment.validation_code = stripe_charge_token
#             payment.save()
#
#             # set order status to sold and save the order
#             self.status = 'sold'
#             self.save()
#
#             for order_item in self.active_items(include_tax_item=False):
#                 if type(order_item.Product) is BulkProduct:
#                     # update product quantities for BulkProducts
#                     order_item.Product.quantity -= order_item.quantity
#                 elif type(order_item.Product) is IndividualProduct:
#                     # update status for IndividualProducts
#                     order_item.Product.status = 2
#                 order_item.save()
#
#
# class OrderItem(PolymorphicModel):
#     '''A line item on an order'''
#     STATUS_CHOICES = (
#         ('active', 'Active'),
#         ('deleted', 'Deleted'),
#     )
#     order = models.ForeignKey(
#         Order, related_name="items", on_delete=models.CASCADE)
#     status = models.TextField(choices=STATUS_CHOICES,
#                               default='active', db_index=True)
#     product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
#     description = models.TextField(null=True, blank=True)
#     # max number is 999,999.99
#     price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
#     quantity = models.IntegerField(default=0)
#     # max number is 999,999.99 (p x q)
#     extended = models.DecimalField(max_digits=8, decimal_places=2, default=0)
#
#     def __str__(self):
#         '''Prints for debugging purposes'''
#         return 'OrderItem {}: {}: {}'.format(self.id, self.product.name, self.extended)
#
#     def recalculate(self):
#         '''Updates the order item's price, quantity, extended'''
#         # update the price if it isn't already set and we have a product
#
#         # default the quantity to 1 if we don't have a quantity set
#
#         # calculate the extended (price * quantity)
#         self.extended = self.price * self.quantity
#         # save the changes
#         self.save()
#
#
# class Payment(models.Model):
#     '''A payment on a sale'''
#     order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE)
#     payment_date = models.DateTimeField(null=True, blank=True)
#     amount = models.DecimalField(
#         blank=True, null=True, max_digits=8, decimal_places=2)  # max number is 999,999.99
#     validation_code = models.TextField(null=True, blank=True)

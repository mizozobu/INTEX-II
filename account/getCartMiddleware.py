from django_mako_plus import view_function
from catalog import models as c
from account import models as a


@view_function
class GetCartMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before the view (and later middleware) are called.
        if request.user.is_authenticated:
            request.cart = c.Order.objects.filter(user=a.User.objects.get(email=request.user)).filter(status="cart").first()

        response = self.get_response(request)
        # Code to be executed for each request/response after the view is called.
        # save to session

        if request.user.is_authenticated:
            request.cart = c.Order.objects.filter(user=a.User.objects.get(email=request.user)).filter(status="cart").first()

        return response

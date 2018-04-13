from django_mako_plus import view_function
from catalog import models as m


@view_function
class LastFiveMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before the view (and later middleware) are called.
        last_five_id = request.session.get('last_five', [])
        request.last_five_p = []

        last_five_id = last_five_id[:5]

        for id in last_five_id:
            request.last_five_p.append(m.Product.objects.get(id=id))

        response = self.get_response(request)

        # Code to be executed for each request/response after the view is called.
        # save to session
        if request.dmp.app == 'catalog' and request.dmp.page == 'detail':
            id = int(request.dmp.urlparams[0])
            if last_five_id is None:
                last_five_id = [id]
            else:
                if id in last_five_id:
                    last_five_id.remove(id)
                last_five_id.insert(0, id)

            request.session['last_five'] = last_five_id

        return response

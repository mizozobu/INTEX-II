from django_mako_plus import view_function
from django.http import HttpResponseRedirect
from django.contrib.auth import logout


@view_function
def process_request(request):
    redirect_to = request.GET.get('next', '')
    logout(request)
    return HttpResponseRedirect(redirect_to)

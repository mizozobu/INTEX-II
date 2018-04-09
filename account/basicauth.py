from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied
from account import models as amod
from base64 import b64decode

import logging
log = logging.getLogger('django')

HEADER_KEY = 'HTTP_AUTHORIZATION'


class BasicAuthMiddleware:
    '''Logs the user in using basic auth'''
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # see if the header is in the request
        header = request.META.get(HEADER_KEY)
        log.info('BasicAuthMiddleware: HTTP_AUTHORIZATION header is "%s"', header)
        if header is not None:
            parts = header.split(' ')
            if parts[0].lower() == 'basic' and len(parts) >= 2:
                auth = b64decode(parts[1]).decode().split(':')
                log.info('BasicAuthMiddleware: email, password is %s', auth)
                if len(auth) >= 2:
                    user = authenticate(email=auth[0], password=auth[1])
                    if user is not None:
                        login(request, user)
                        log.info('BasicAuthMiddleware: success...logged in %s', user.get_full_name)
                    else:
                        log.info('BasicAuthMiddleware: failed...email or password did not match')
                        raise PermissionDenied('Invalid email or password in HTTP Basic Authentication')

        # let the request/response continue
        response = self.get_response(request)

        return response

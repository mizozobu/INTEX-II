# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523310276.8885422
_enable_loop = True
_template_filename = 'C:/INTEX-II-hilarySprint7/homepage/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['header', 'footer']


from catalog import models as cmod 

from account import models as amod 

from datetime import datetime 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        str = context.get('str', UNDEFINED)
        null = context.get('null', UNDEFINED)
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\n')
        __M_writer('\r\n\n')
        __M_writer('\r\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        str = context.get('str', UNDEFINED)
        null = context.get('null', UNDEFINED)
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\n<nav class="navbar fixed-top navbar-light bg-faded">\n    \r\n<a class="navbar-brand" href="/homepage/">\n        \r\n<img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/images/logo.png" width="70" height="70" alt="family oriented music organization">\n    \r\n</a>\n    \r\n<ul class="nav nav-pills">\n        \r\n<li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'homepage' and request.dmp.page == 'index' else '' ))
        __M_writer('" href="/homepage/index/">Home</a></li>\n        \r\n<li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'homepage' and request.dmp.page == 'about' else '' ))
        __M_writer('" href="/homepage/about/">About</a></li>\n        \r\n<li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'homepage' and request.dmp.page == 'faq' else '' ))
        __M_writer('" href="/homepage/faq/">FAQ</a></li>\n        \r\n<li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'homepage' and request.dmp.page == 'terms' else '' ))
        __M_writer('" href="/homepage/terms/">Terms</a></li>\n        \r\n<li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'homepage' and request.dmp.page == 'contact' else '' ))
        __M_writer('" href="/homepage/contact/">Contact</a></li>\n        \r\n')
        cart = cmod.Order.objects.all().filter(user=amod.User.objects.get(email=request.user)).filter(status="cart").first() if request.user.is_authenticated else null
        
        __M_writer('\n        \r\n\r\n<!--<li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'catalog' and request.dmp.page == 'cart' else ''))
        __M_writer('href="/catalog/cart/')
        __M_writer(str(cart.id))
        __M_writer('"> ')
        __M_writer(str("Shopping Cart (" + str(cart.num_items()) + ")"))
        __M_writer('</a></li>\n   -->\r\n \r\n')
        if  request.user.is_authenticated:
            __M_writer('        \r\n<li class="nav-item dropdown">\n            \r\n<button class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">My Account</button>\n            \r\n<div class="dropdown-menu">\n                \r\n<a class="dropdown-item" href="/account/logout/">Log Out</a>\n            \r\n</div>\n        </li>\n        \r\n')
        else:
            __M_writer('        <li class="nav-item dropdown">\n            \r\n<button class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Log In</button>\n            <div class="dropdown-menu">\n                <a class="dropdown-item" href="/account/signup/">Sign Up</a>\n                <a class="dropdown-item" href="/account/login/">Log In</a>\n            </div>\n        </li>\n')
        __M_writer('    </ul>\n</nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\n    <p class="footer-text">\n        ')
        __M_writer('\n        &copy; FOMO ')
        __M_writer(str( datetime.now().year ))
        __M_writer('. All rights reserved.\n    </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/INTEX-II-hilarySprint7/homepage/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"18": 3, "20": 5, "22": 64, "35": 0, "48": 1, "49": 3, "50": 5, "55": 60, "60": 67, "66": 8, "76": 8, "77": 13, "78": 13, "79": 19, "80": 19, "81": 21, "82": 21, "83": 23, "84": 23, "85": 25, "86": 25, "87": 27, "88": 27, "89": 29, "91": 29, "92": 32, "93": 32, "94": 32, "95": 32, "96": 32, "97": 32, "98": 35, "99": 36, "100": 48, "101": 49, "102": 58, "108": 62, "114": 62, "115": 64, "116": 65, "117": 65, "123": 117}}
__M_END_METADATA
"""

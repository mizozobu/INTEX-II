# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523293335.729767
_enable_loop = True
_template_filename = '/mnt/c/Users/hilar/OneDrive - BYU Office 365/IS413/INTEX-II/homepage/templates/app_base.htm'
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
        Undefined = context.get('Undefined', UNDEFINED)
        request = context.get('request', UNDEFINED)
        str = context.get('str', UNDEFINED)
        null = context.get('null', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
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
        Undefined = context.get('Undefined', UNDEFINED)
        request = context.get('request', UNDEFINED)
        str = context.get('str', UNDEFINED)
        null = context.get('null', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\n<nav class="navbar fixed-top navbar-light bg-faded">\n    <a class="navbar-brand" href="/homepage/">\n        <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/images/logo.png" width="70" height="70" alt="family oriented music organization">\n    </a>\n    <ul class="nav nav-pills">\n        <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'homepage' and request.dmp.page == 'index' else '' ))
        __M_writer('" href="/homepage/index/">Home</a></li>\n        <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'homepage' and request.dmp.page == 'about' else '' ))
        __M_writer('" href="/homepage/about/">About</a></li>\n        <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'homepage' and request.dmp.page == 'faq' else '' ))
        __M_writer('" href="/homepage/faq/">FAQ</a></li>\n        <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'homepage' and request.dmp.page == 'terms' else '' ))
        __M_writer('" href="/homepage/terms/">Terms</a></li>\n        <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'homepage' and request.dmp.page == 'contact' else '' ))
        __M_writer('" href="/homepage/contact/">Contact</a></li>\n        ')
        cart = cmod.Order.objects.all().filter(user=amod.User.objects.get(email=request.user)).filter(status="cart").first() if request.user.is_authenticated else null
        
        __M_writer('\n        <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'catalog' and request.dmp.page == 'cart' else ''))
        __M_writer('href="/catalog/cart/')
        __M_writer(str(0 if cart is Undefined else cart.id))
        __M_writer('"> ')
        __M_writer(str("Shopping Cart (" + str(cart.num_items()) + ")" if cart is not Undefined else ""))
        __M_writer('</a></li>\n')
        if  request.user.is_authenticated:
            __M_writer('        <li class="nav-item dropdown">\n            <button class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">My Account</button>\n            <div class="dropdown-menu">\n                <a class="dropdown-item" href="/account/logout/">Log Out</a>\n            </div>\n        </li>\n')
        else:
            __M_writer('        <li class="nav-item dropdown">\n            <button class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Log In</button>\n            <div class="dropdown-menu">\n                <a class="dropdown-item" href="/account/signup/">Sign Up</a>\n                <a class="dropdown-item" href="/account/login/">Log In</a>\n            </div>\n        </li>\n')
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
{"line_map": {"67": 5, "22": 40, "78": 5, "79": 8, "80": 8, "81": 11, "82": 11, "83": 12, "20": 3, "85": 13, "86": 13, "87": 14, "88": 14, "89": 15, "90": 15, "91": 16, "93": 16, "94": 17, "95": 17, "96": 17, "97": 17, "98": 17, "35": 0, "100": 18, "101": 19, "102": 25, "103": 26, "104": 34, "18": 2, "110": 38, "125": 119, "99": 17, "49": 1, "50": 2, "51": 3, "116": 38, "117": 40, "118": 41, "119": 41, "56": 36, "84": 12, "61": 43}, "source_encoding": "utf-8", "filename": "/mnt/c/Users/hilar/OneDrive - BYU Office 365/IS413/INTEX-II/homepage/templates/app_base.htm", "uri": "app_base.htm"}
__M_END_METADATA
"""

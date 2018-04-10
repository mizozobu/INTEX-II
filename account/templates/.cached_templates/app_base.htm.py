# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523319375.7599187
_enable_loop = True
_template_filename = '/mnt/c/Users/hilar/OneDrive - BYU Office 365/IS413/INTEX-II/account/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['footer', 'header']


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
    return runtime._inherit_from(context, 'homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def footer():
            return render_footer(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        null = context.get('null', UNDEFINED)
        request = context.get('request', UNDEFINED)
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


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def header():
            return render_header(context)
        null = context.get('null', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<nav class="navbar fixed-top navbar-light bg-faded">\n    <a class="navbar-brand" href="/homepage/">\n        <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/images/logo.png" width="70" height="70" alt="logo.png">\n    </a>\n    <ul class="nav nav-pills">\n        <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.page == 'index' else '' ))
        __M_writer('" href="/index/">Home</a></li>\n        <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.page == 'about' else '' ))
        __M_writer('" href="/about/">About</a></li>\n        <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.page == 'faq' else '' ))
        __M_writer('" href="/faq/">FAQ</a></li>\n        <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.page == 'terms' else '' ))
        __M_writer('" href="/terms/">Terms</a></li>\n        <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.page == 'contact' else '' ))
        __M_writer('" href="/contact/">Contact</a></li>\n        ')
        cart = cmod.Order.objects.all().filter(user=amod.User.objects.get(email=request.user)).filter(status="cart").first() if request.user.is_authenticated else null
        
        __M_writer('\n')
        if (cart is not null) and (cart is not None) and (cart.num_items() > 0):
            __M_writer('        <li class="')
            __M_writer(str( 'active' if request.dmp.page == '/catalog/cart' else ''))
            __M_writer('"><a href="/catalog/cart/')
            __M_writer(str(cart.id))
            __M_writer('">Shopping Cart (')
            __M_writer(str(cart.num_items()))
            __M_writer(')</a></li>\n')
        if  request.user.is_authenticated:
            __M_writer('        <li class="nav-item dropdown">\n            <button class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">My Account</button>\n            <div class="dropdown-menu">\n                <a class="dropdown-item" href="/account/logout/">Log Out</a>\n            </div>\n        </li>\n')
        if  not request.user.is_authenticated:
            __M_writer('        <li class="nav-item dropdown">\n            <button class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Log In</button>\n            <div class="dropdown-menu">\n                <a class="dropdown-item" href="/account/signup/">Sign Up</a>\n                <a class="dropdown-item" href="/account/login/">Log In</a>\n            </div>\n        </li>\n')
        __M_writer('    </ul>\n</nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"18": 2, "20": 3, "22": 43, "35": 0, "47": 1, "48": 2, "49": 3, "54": 39, "59": 46, "65": 41, "71": 41, "72": 43, "73": 44, "74": 44, "80": 5, "89": 5, "90": 8, "91": 8, "92": 11, "93": 11, "94": 12, "95": 12, "96": 13, "97": 13, "98": 14, "99": 14, "100": 15, "101": 15, "102": 16, "104": 16, "105": 17, "106": 18, "107": 18, "108": 18, "109": 18, "110": 18, "111": 18, "112": 18, "113": 20, "114": 21, "115": 28, "116": 29, "117": 37, "123": 117}, "filename": "/mnt/c/Users/hilar/OneDrive - BYU Office 365/IS413/INTEX-II/account/templates/app_base.htm", "source_encoding": "utf-8", "uri": "app_base.htm"}
__M_END_METADATA
"""

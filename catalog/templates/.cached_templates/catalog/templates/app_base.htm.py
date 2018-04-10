# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523318579.4568226
_enable_loop = True
_template_filename = '/mnt/c/Users/hilar/OneDrive - BYU Office 365/IS413/INTEX-II/catalog/templates/app_base.htm'
_template_uri = 'catalog/templates/app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['header', 'footer', 'right', 'left']


from catalog import models as m 

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
        range = context.get('range', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def right():
            return render_right(context._locals(__M_locals))
        def left():
            return render_left(context._locals(__M_locals))
        category_id = context.get('category_id', UNDEFINED)
        null = context.get('null', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right'):
            context['self'].right(**pageargs)
        

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
        def header():
            return render_header(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        null = context.get('null', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <nav class="navbar fixed-top navbar-light bg-faded">\n        <a class="navbar-brand" href="/homepage/">\n            <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/images/logo.png" width="70" height="70" alt="family oriented music organization">\n        </a>\n        <ul class="nav nav-pills">\n            <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'homepage' and request.dmp.page == 'index' else '' ))
        __M_writer('" href="/homepage/index/">Home</a></li>\n            <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'homepage' and request.dmp.page == 'about' else '' ))
        __M_writer('" href="/homepage/about/">About</a></li>\n            <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'homepage' and request.dmp.page == 'faq' else '' ))
        __M_writer('" href="/homepage/faq/">FAQ</a></li>\n            <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'homepage' and request.dmp.page == 'terms' else '' ))
        __M_writer('" href="/homepage/terms/">Terms</a></li>\n            <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'homepage' and request.dmp.page == 'contact' else '' ))
        __M_writer('" href="/homepage/contact/">Contact</a></li>\n            ')
        cart = m.Order.objects.all().filter(user=amod.User.objects.get(email=request.user)).filter(status="cart").first() if request.user.is_authenticated else null
        
        __M_writer('\n')
        if (cart is not null) and (cart is not None) and (cart.num_items() > 0):
            __M_writer('            <li class="')
            __M_writer(str( 'active' if request.dmp.page == '/catalog/cart' else ''))
            __M_writer('"><a href="/catalog/cart/')
            __M_writer(str(cart.id))
            __M_writer('">Shopping Cart (')
            __M_writer(str(cart.num_items()))
            __M_writer(')</a></li>\n')
        if  request.user.is_authenticated:
            __M_writer('            <li class="nav-item dropdown">\n                <button class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">My Account</button>\n                <div class="dropdown-menu">\n                    <a class="dropdown-item" href="/account/logout/">Log Out</a>\n                </div>\n            </li>\n')
        else:
            __M_writer('            <li class="nav-item dropdown">\n                <button class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Log In</button>\n                <div class="dropdown-menu">\n                    <a class="dropdown-item" href="/account/signup/">Sign Up</a>\n                    <a class="dropdown-item" href="/account/login/">Log In</a>\n                </div>\n            </li>\n')
        __M_writer('        </ul>\n    </nav>\n')
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


def render_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        range = context.get('range', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def right():
            return render_right(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="content right">\n        <div id="right-container">\n            <p class="right-heading">View History</p>\n            <ol class="history">\n')
        for i in range(len(request.last_five_p)):
            __M_writer('                    <a href="/catalog/detail/')
            __M_writer(str(request.last_five_p[i].id))
            __M_writer('">\n                        <li class="viewed-item">\n                            <img src="')
            __M_writer(str(request.last_five_p[i].image_url()))
            __M_writer('" alt=')
            __M_writer(str(request.last_five_p[i].name))
            __M_writer('>\n                            <p class="name">')
            __M_writer(filters.html_escape(str(request.last_five_p[i].name )))
            __M_writer('</p>\n                            <p class="price">&dollar;')
            __M_writer(str(request.last_five_p[i].price))
            __M_writer('</p>\n                        </li>\n                    </a>\n')
        __M_writer('            </ol>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        category_id = context.get('category_id', UNDEFINED)
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="content left">\n        <ul class="category-list">\n            <a id="all-product" href="/catalog/index/"><li>All Products</li></a>\n')
        for c in m.Category.objects.all():
            __M_writer('                <a href="/catalog/index/')
            __M_writer(str(c.id))
            __M_writer('/" class="cat ')
            __M_writer(str('active' if category_id == c.id else '' ))
            __M_writer('"><li>')
            __M_writer(filters.html_escape(str(c.name )))
            __M_writer('</li></a>\n')
        __M_writer('        </ul>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/mnt/c/Users/hilar/OneDrive - BYU Office 365/IS413/INTEX-II/catalog/templates/app_base.htm", "uri": "catalog/templates/app_base.htm", "line_map": {"131": 70, "132": 72, "133": 73, "134": 73, "140": 51, "18": 2, "20": 3, "149": 51, "22": 72, "151": 57, "152": 57, "153": 57, "154": 59, "155": 59, "156": 59, "157": 59, "150": 56, "159": 60, "160": 61, "161": 61, "162": 65, "35": 0, "168": 40, "175": 40, "176": 44, "177": 45, "178": 45, "179": 45, "180": 45, "158": 60, "54": 1, "55": 2, "56": 3, "61": 38, "190": 184, "181": 45, "66": 49, "182": 45, "71": 68, "183": 45, "76": 75, "184": 47, "82": 5, "91": 5, "92": 8, "93": 8, "94": 11, "95": 11, "96": 12, "97": 12, "98": 13, "99": 13, "100": 14, "101": 14, "102": 15, "103": 15, "104": 16, "106": 16, "107": 17, "108": 18, "109": 18, "110": 18, "111": 18, "112": 18, "113": 18, "114": 18, "115": 20, "116": 21, "117": 27, "118": 28, "119": 36, "125": 70}, "source_encoding": "utf-8"}
__M_END_METADATA
"""

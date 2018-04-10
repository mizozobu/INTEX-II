# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523331002.3245852
_enable_loop = True
_template_filename = 'C:/users/scott laptop/documents/mariah/intex/intex-ii/catalog/templates/app_base.htm'
_template_uri = 'catalog/templates/app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['header', 'left', 'right', 'footer']


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
        def left():
            return render_left(context._locals(__M_locals))
        null = context.get('null', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def right():
            return render_right(context._locals(__M_locals))
        range = context.get('range', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        category_id = context.get('category_id', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right'):
            context['self'].right(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        null = context.get('null', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def header():
            return render_header(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <nav class="navbar fixed-top navbar-light bg-faded">\r\n        <a class="navbar-brand" href="/homepage/">\r\n            <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/images/logo.png" width="70" height="70" alt="family oriented music organization">\r\n        </a>\r\n        <ul class="nav nav-pills">\r\n            <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'homepage' and request.dmp.page == 'index' else '' ))
        __M_writer('" href="/homepage/index/">Home</a></li>\r\n            <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'homepage' and request.dmp.page == 'about' else '' ))
        __M_writer('" href="/homepage/about/">About</a></li>\r\n            <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'homepage' and request.dmp.page == 'faq' else '' ))
        __M_writer('" href="/homepage/faq/">FAQ</a></li>\r\n            <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'homepage' and request.dmp.page == 'terms' else '' ))
        __M_writer('" href="/homepage/terms/">Terms</a></li>\r\n            <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'homepage' and request.dmp.page == 'contact' else '' ))
        __M_writer('" href="/homepage/contact/">Contact</a></li>\r\n            ')
        cart = m.Order.objects.all().filter(user=amod.User.objects.get(email=request.user)).filter(status="cart").first() if request.user.is_authenticated else null
        
        __M_writer('\r\n')
        if (cart is not null) and (cart is not None) and (cart.num_items() > 0):
            __M_writer('            <li class="')
            __M_writer(str( 'active' if request.dmp.page == '/catalog/cart' else ''))
            __M_writer('"><a href="/catalog/cart/')
            __M_writer(str(cart.id))
            __M_writer('">Shopping Cart (')
            __M_writer(str(cart.num_items()))
            __M_writer(')</a></li>\r\n')
        if  request.user.is_authenticated:
            __M_writer('            <li class="nav-item dropdown">\r\n                <button class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">My Account</button>\r\n                <div class="dropdown-menu">\r\n                    <a class="dropdown-item" href="/account/logout/">Log Out</a>\r\n                </div>\r\n            </li>\r\n')
        else:
            __M_writer('            <li class="nav-item dropdown">\r\n                <button class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Log In</button>\r\n                <div class="dropdown-menu">\r\n                    <a class="dropdown-item" href="/account/signup/">Sign Up</a>\r\n                    <a class="dropdown-item" href="/account/login/">Log In</a>\r\n                </div>\r\n            </li>\r\n')
        __M_writer('        </ul>\r\n    </nav>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        category_id = context.get('category_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content left">\r\n        <ul class="category-list">\r\n            <a id="all-product" href="/catalog/index/"><li>All Products</li></a>\r\n')
        for c in m.Category.objects.all():
            __M_writer('                <a href="/catalog/index/')
            __M_writer(str(c.id))
            __M_writer('/" class="cat ')
            __M_writer(str('active' if category_id == c.id else '' ))
            __M_writer('"><li>')
            __M_writer(filters.html_escape(str(c.name )))
            __M_writer('</li></a>\r\n')
        __M_writer('        </ul>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        def right():
            return render_right(context)
        range = context.get('range', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content right">\r\n        <div id="right-container">\r\n            <p class="right-heading">View History</p>\r\n            <ol class="history">\r\n')
        for i in range(len(request.last_five_p)):
            __M_writer('                    <a href="/catalog/detail/')
            __M_writer(str(request.last_five_p[i].id))
            __M_writer('">\r\n                        <li class="viewed-item">\r\n                            <img src="')
            __M_writer(str(request.last_five_p[i].image_url()))
            __M_writer('" alt=')
            __M_writer(str(request.last_five_p[i].name))
            __M_writer('>\r\n                            <p class="name">')
            __M_writer(filters.html_escape(str(request.last_five_p[i].name )))
            __M_writer('</p>\r\n                            <p class="price">&dollar;')
            __M_writer(str(request.last_five_p[i].price))
            __M_writer('</p>\r\n                        </li>\r\n                    </a>\r\n')
        __M_writer('            </ol>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <p class="footer-text">\r\n        ')
        __M_writer('\r\n        &copy; FOMO ')
        __M_writer(str( datetime.now().year ))
        __M_writer('. All rights reserved.\r\n    </p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/users/scott laptop/documents/mariah/intex/intex-ii/catalog/templates/app_base.htm", "uri": "catalog/templates/app_base.htm", "source_encoding": "utf-8", "line_map": {"18": 2, "20": 3, "22": 72, "35": 0, "54": 1, "55": 2, "56": 3, "61": 38, "66": 49, "71": 68, "76": 75, "82": 5, "91": 5, "92": 8, "93": 8, "94": 11, "95": 11, "96": 12, "97": 12, "98": 13, "99": 13, "100": 14, "101": 14, "102": 15, "103": 15, "104": 16, "106": 16, "107": 17, "108": 18, "109": 18, "110": 18, "111": 18, "112": 18, "113": 18, "114": 18, "115": 20, "116": 21, "117": 27, "118": 28, "119": 36, "125": 40, "132": 40, "133": 44, "134": 45, "135": 45, "136": 45, "137": 45, "138": 45, "139": 45, "140": 45, "141": 47, "147": 51, "156": 51, "157": 56, "158": 57, "159": 57, "160": 57, "161": 59, "162": 59, "163": 59, "164": 59, "165": 60, "166": 60, "167": 61, "168": 61, "169": 65, "175": 70, "181": 70, "182": 72, "183": 73, "184": 73, "190": 184}}
__M_END_METADATA
"""

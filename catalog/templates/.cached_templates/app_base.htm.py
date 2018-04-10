# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523388470.4143682
_enable_loop = True
_template_filename = 'C:/users/Scott Laptop/documents/Mariah/intex/intex-ii/catalog/templates/app_base.htm'
_template_uri = 'app_base.htm'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        null = context.get('null', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        def right():
            return render_right(context._locals(__M_locals))
        len = context.get('len', UNDEFINED)
        range = context.get('range', UNDEFINED)
        category_id = context.get('category_id', UNDEFINED)
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
        def header():
            return render_header(context)
        request = context.get('request', UNDEFINED)
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
        __M_writer('" href="/homepage/contact/">Contact</a></li>\r\n            <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'catalog' and request.dmp.page == 'index' else '' ))
        __M_writer('" href="/catalog/index/">Catalog</a></li>\r\n            ')
        cart = m.Order.objects.all().filter(user=amod.User.objects.get(email=request.user)).filter(status="cart").first() if request.user.is_authenticated else null
        
        __M_writer('\r\n')
        if (cart is not null) and (cart is not None) and (cart.num_items() > 0):
            __M_writer('            <li class="')
            __M_writer(str( 'active nav-item' if request.dmp.page == '/catalog/cart' else ''))
            __M_writer('"><a href="/catalog/cart/')
            __M_writer(str(cart.id))
            __M_writer('" class="nav-link">Shopping Cart (')
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
        category_id = context.get('category_id', UNDEFINED)
        def left():
            return render_left(context)
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
        def right():
            return render_right(context)
        range = context.get('range', UNDEFINED)
        request = context.get('request', UNDEFINED)
        len = context.get('len', UNDEFINED)
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
{"filename": "C:/users/Scott Laptop/documents/Mariah/intex/intex-ii/catalog/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"18": 2, "20": 3, "22": 73, "35": 0, "54": 1, "55": 2, "56": 3, "61": 39, "66": 50, "71": 69, "76": 76, "82": 5, "91": 5, "92": 8, "93": 8, "94": 11, "95": 11, "96": 12, "97": 12, "98": 13, "99": 13, "100": 14, "101": 14, "102": 15, "103": 15, "104": 16, "105": 16, "106": 17, "108": 17, "109": 18, "110": 19, "111": 19, "112": 19, "113": 19, "114": 19, "115": 19, "116": 19, "117": 21, "118": 22, "119": 28, "120": 29, "121": 37, "127": 41, "134": 41, "135": 45, "136": 46, "137": 46, "138": 46, "139": 46, "140": 46, "141": 46, "142": 46, "143": 48, "149": 52, "158": 52, "159": 57, "160": 58, "161": 58, "162": 58, "163": 60, "164": 60, "165": 60, "166": 60, "167": 61, "168": 61, "169": 62, "170": 62, "171": 66, "177": 71, "183": 71, "184": 73, "185": 74, "186": 74, "192": 186}}
__M_END_METADATA
"""

# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523403112.5472615
_enable_loop = True
_template_filename = 'C:/users/Scott Laptop/documents/Mariah/intex/intex-ii/manager/templates/app_base.htm'
_template_uri = 'manager/templates/app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['header']


from catalog import models as m 

from account import models as amod 

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
    return runtime._inherit_from(context, '/catalog/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        null = context.get('null', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        null = context.get('null', UNDEFINED)
        def header():
            return render_header(context)
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
        __M_writer('" href="/catalog/index/">Shop</a></li>\r\n            ')
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
        if request.user.is_authenticated:
            __M_writer('            <li class="nav-item dropdown">\r\n                <button class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">My Account</button>\r\n                <div class="dropdown-menu">\r\n                  ')
            currentUser = amod.User.objects.get(id=request.user.id) 
            
            __M_writer('\r\n')
            if currentUser.is_staff == True:
                __M_writer('                    <a class="dropdown-item" href="/manager/index/">Edit Products</a>\r\n')
            __M_writer('                    <a class="dropdown-item" href="/manager/index/">Edit Products</a>\r\n\r\n                    <a class="dropdown-item" href="/account/logout/">Log Out</a>\r\n                </div>\r\n            </li>\r\n')
        else:
            __M_writer('            <li class="nav-item dropdown">\r\n                <button class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Log In</button>\r\n                <div class="dropdown-menu">\r\n                    <a class="dropdown-item" href="/account/signup/">Sign Up</a>\r\n                    <a class="dropdown-item" href="/account/login/">Log In</a>\r\n                </div>\r\n            </li>\r\n')
        __M_writer('        </ul>\r\n    </nav>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/users/Scott Laptop/documents/Mariah/intex/intex-ii/manager/templates/app_base.htm", "uri": "manager/templates/app_base.htm", "source_encoding": "utf-8", "line_map": {"18": 2, "20": 3, "33": 0, "43": 1, "44": 2, "45": 3, "50": 45, "56": 5, "65": 5, "66": 8, "67": 8, "68": 11, "69": 11, "70": 12, "71": 12, "72": 13, "73": 13, "74": 14, "75": 14, "76": 15, "77": 15, "78": 16, "79": 16, "80": 17, "82": 17, "83": 18, "84": 19, "85": 19, "86": 19, "87": 19, "88": 19, "89": 19, "90": 19, "91": 21, "92": 22, "93": 25, "95": 25, "96": 26, "97": 27, "98": 29, "99": 34, "100": 35, "101": 43, "107": 101}}
__M_END_METADATA
"""

# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520457192.9923556
_enable_loop = True
_template_filename = 'C:/Users/hamcm/Desktop/S0/fomo/homepage/templates/app_base.htm'
_template_uri = 'homepage/templates/app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['header', 'footer']


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
        request = context.get('request', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

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
        request = context.get('request', UNDEFINED)
        def header():
            return render_header(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<nav class="navbar fixed-top navbar-light bg-faded">\r\n    <a class="navbar-brand" href="/homepage/">\r\n        <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/images/logo.png" width="70" height="70" alt="family oriented music organization">\r\n    </a>\r\n    <ul class="nav nav-pills">\r\n        <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'homepage' and request.dmp.page == 'index' else '' ))
        __M_writer('" href="/homepage/index/">Home</a></li>\r\n        <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'homepage' and request.dmp.page == 'about' else '' ))
        __M_writer('" href="/homepage/about/">About</a></li>\r\n        <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'homepage' and request.dmp.page == 'faq' else '' ))
        __M_writer('" href="/homepage/faq/">FAQ</a></li>\r\n        <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'homepage' and request.dmp.page == 'terms' else '' ))
        __M_writer('" href="/homepage/terms/">Terms</a></li>\r\n        <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.app == 'homepage' and request.dmp.page == 'contact' else '' ))
        __M_writer('" href="/homepage/contact/">Contact</a></li>\r\n')
        if  request.user.is_authenticated:
            __M_writer('        <li class="nav-item dropdown">\r\n            <button class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">My Account</button>\r\n            <div class="dropdown-menu">\r\n                <a class="dropdown-item" href="/account/logout/">Log Out</a>\r\n            </div>\r\n        </li>\r\n')
        if  not request.user.is_authenticated:
            __M_writer('        <li class="nav-item dropdown">\r\n            <button class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Log In</button>\r\n            <div class="dropdown-menu">\r\n                <a class="dropdown-item" href="/account/signup/">Sign Up</a>\r\n                <a class="dropdown-item" href="/account/login/">Log In</a>\r\n            </div>\r\n        </li>\r\n')
        __M_writer('    </ul>\r\n</nav>\r\n')
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
{"filename": "C:/Users/hamcm/Desktop/S0/fomo/homepage/templates/app_base.htm", "uri": "homepage/templates/app_base.htm", "source_encoding": "utf-8", "line_map": {"18": 37, "31": 0, "42": 1, "47": 33, "52": 40, "58": 3, "66": 3, "67": 6, "68": 6, "69": 9, "70": 9, "71": 10, "72": 10, "73": 11, "74": 11, "75": 12, "76": 12, "77": 13, "78": 13, "79": 14, "80": 15, "81": 22, "82": 23, "83": 31, "89": 35, "95": 35, "96": 37, "97": 38, "98": 38, "104": 98}}
__M_END_METADATA
"""

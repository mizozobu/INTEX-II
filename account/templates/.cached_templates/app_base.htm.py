# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1518209910.7080207
_enable_loop = True
_template_filename = 'C:/Users/hamcm/desktop/s0/fomo/account/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
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
    return runtime._inherit_from(context, 'homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def footer():
            return render_footer(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
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
        __M_writer('homepage/media/images/logo.png" width="70" height="70" alt="logo.png">\r\n    </a>\r\n    <ul class="nav nav-pills">\r\n        <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.page == 'index' else '' ))
        __M_writer('" href="/index/">Home</a></li>\r\n        <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.page == 'about' else '' ))
        __M_writer('" href="/about/">About</a></li>\r\n        <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.page == 'faq' else '' ))
        __M_writer('" href="/faq/">FAQ</a></li>\r\n        <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.page == 'terms' else '' ))
        __M_writer('" href="/terms/">Terms</a></li>\r\n        <li class="nav-item"><a class="nav-link ')
        __M_writer(str('active' if request.dmp.page == 'contact' else '' ))
        __M_writer('" href="/contact/">Contact</a></li>\r\n')
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
{"filename": "C:/Users/hamcm/desktop/s0/fomo/account/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"17": 37, "30": 0, "41": 1, "46": 33, "51": 40, "57": 3, "65": 3, "66": 6, "67": 6, "68": 9, "69": 9, "70": 10, "71": 10, "72": 11, "73": 11, "74": 12, "75": 12, "76": 13, "77": 13, "78": 14, "79": 15, "80": 22, "81": 23, "82": 31, "88": 35, "94": 35, "95": 37, "96": 38, "97": 38, "103": 97}}
__M_END_METADATA
"""

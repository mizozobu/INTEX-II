# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523465954.9386766
_enable_loop = True
_template_filename = 'C:/Users/Scott Laptop/Documents/Mariah/intex/intex-ii/catalog/templates/base.htm'
_modified_time = 1523465688.4082532
_enable_loop = True
_template_filename = 'C:/INTEX-II/catalog/templates/base.htm'
_template_uri = '/catalog/templates/base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['addonlink', 'maintenanceMessage', 'header', 'top', 'left', 'center', 'right', 'bottom', 'footer']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)

        def addonlink():
            return render_addonlink(context._locals(__M_locals))
        def bottom():
            return render_bottom(context._locals(__M_locals))
        def maintenanceMessage():
            return render_maintenanceMessage(context._locals(__M_locals))
        def left():
            return render_left(context._locals(__M_locals))

        def center():
            return render_center(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))

        def header():
            return render_header(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def top():
            return render_top(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def left():
            return render_left(context._locals(__M_locals))
        def right():
            return render_right(context._locals(__M_locals))

        def addonlink():
            return render_addonlink(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def right():
            return render_right(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        def bottom():
            return render_bottom(context._locals(__M_locals))
        def top():
            return render_top(context._locals(__M_locals))
        def maintenanceMessage():
            return render_maintenanceMessage(context._locals(__M_locals))

        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n        <title>FOMO</title>\r\n\r\n')
        __M_writer('        <link rel="icon" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/favicon.ico" type="image/x-icon"/>\r\n\r\n')
        __M_writer('        <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap/css/bootstrap-grid.min.css">\r\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap/css/bootstrap-grid.css">\r\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap/css/bootstrap.min.css">\r\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap/css/bootstrap.css">\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'addonlink'):
            context['self'].addonlink(**pageargs)


        __M_writer('\r\n')
        __M_writer('        <script src="//ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\r\n\r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(str( django_mako_plus.links(self) ))
        __M_writer('\r\n    </head>\r\n    <body>\r\n        <div id="page">\r\n            <a class="d-none" href="#content">skip to content</a>\r\n\r\n            <div class="container">\r\n              <div class="row">\r\n                <div class="row">\r\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'maintenanceMessage'):
            context['self'].maintenanceMessage(**pageargs)


        __M_writer('\r\n                </div>\r\n              </div>\r\n            </div>\r\n\r\n            <header>\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)


        __M_writer('\r\n            </header>\r\n\r\n            <main class="mainBox">\r\n\r\n              <div class="row">\r\n                  <div class="col-md-12" id="top">\r\n                      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)


        __M_writer('\r\n                  </div>\r\n              </div>\r\n\r\n\r\n            <div class="row top-buffer">\r\n                <div class="col-md-2" id="left">\r\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)


        __M_writer('\r\n                </div>\r\n              <div class="col-md-8"  id="center">\r\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)


        __M_writer('\r\n                </div>\r\n\r\n                <div class="col-md-2" id="right">\r\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right'):
            context['self'].right(**pageargs)


        __M_writer('\r\n                </div>\r\n            </div>\r\n\r\n')
        __M_writer('            <div class="row top-buffer">\r\n                <div class="col-md-12" id="bottom">\r\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bottom'):
            context['self'].bottom(**pageargs)


        __M_writer('\r\n                </div>\r\n            </div>\r\n\r\n        </main>\r\n\r\n        </div>\r\n\r\n        <div id="loader-container">\r\n            <span id="loader"></span>\r\n            <p>LOADING ...</p>\r\n        </div>\r\n\r\n    </body>\r\n\r\n    <footer>\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)


        __M_writer('\r\n    </footer>\r\n\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_addonlink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def addonlink():
            return render_addonlink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_maintenanceMessage(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintenanceMessage():
            return render_maintenanceMessage(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top():
            return render_top(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center():
            return render_center(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right():
            return render_right(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bottom(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bottom():
            return render_bottom(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
<<<<<<< HEAD
{"filename": "C:/Users/Scott Laptop/Documents/Mariah/intex/intex-ii/catalog/templates/base.htm", "uri": "/catalog/templates/base.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "43": 2, "44": 9, "45": 9, "46": 9, "47": 12, "48": 12, "49": 12, "50": 13, "51": 13, "52": 14, "53": 14, "54": 15, "55": 15, "60": 16, "61": 18, "62": 21, "63": 22, "64": 22, "69": 31, "74": 37, "79": 44, "84": 51, "89": 54, "94": 58, "95": 63, "100": 65, "105": 81, "111": 16, "122": 31, "133": 37, "144": 44, "155": 51, "166": 54, "177": 58, "188": 65, "199": 81, "210": 199}}
=======
{"filename": "C:/INTEX-II/catalog/templates/base.htm", "uri": "/catalog/templates/base.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "43": 2, "44": 9, "45": 9, "46": 9, "47": 12, "48": 12, "49": 12, "50": 13, "51": 13, "52": 14, "53": 14, "54": 15, "55": 15, "60": 16, "61": 18, "62": 21, "63": 22, "64": 22, "69": 31, "74": 37, "79": 44, "84": 51, "89": 54, "94": 58, "95": 63, "100": 65, "105": 81, "111": 16, "122": 31, "133": 37, "144": 44, "155": 51, "166": 54, "177": 58, "188": 65, "199": 81, "210": 199}}
>>>>>>> 0872055d7c530d4c3ab66f5b7d91b1aec28f8f96
__M_END_METADATA
"""

# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520126546.0400755
_enable_loop = True
_template_filename = 'C:/Users/hamcm/Desktop/S0/fomo/homepage/templates/base.htm'
_template_uri = 'homepage/templates/base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['addonlink', 'maintenanceMessage', 'header', 'top', 'left', 'center', 'right', 'bottom', 'footer']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def top():
            return render_top(context._locals(__M_locals))
        def bottom():
            return render_bottom(context._locals(__M_locals))
        def left():
            return render_left(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def right():
            return render_right(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def center():
            return render_center(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        def maintenanceMessage():
            return render_maintenanceMessage(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        def addonlink():
            return render_addonlink(context._locals(__M_locals))
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
        __M_writer('        <script src="http://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\r\n\r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(str( django_mako_plus.links(self) ))
        __M_writer('\r\n    </head>\r\n    <body>\r\n        <div id="page">\r\n            <a class="d-none" href="#content">skip to content</a>\r\n            <div class="row">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'maintenanceMessage'):
            context['self'].maintenanceMessage(**pageargs)
        

        __M_writer('\r\n            </div>\r\n\r\n            <div class="row">\r\n                <div class="col-sm-12" id="header">\r\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n                </div>\r\n            </div>\r\n\r\n')
        __M_writer('            <div class="row">\r\n                <div class="col-sm-12" id="top">\r\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        __M_writer('\r\n                </div>\r\n            </div>\r\n')
        __M_writer('            <div class="row">\r\n')
        __M_writer('                <div class="col-sm-2" id="left">\r\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\r\n                </div>\r\n')
        __M_writer('                <div class="col-sm-8" id="center">\r\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer('\r\n                </div>\r\n')
        __M_writer('                <div class="col-sm-2" id="right">\r\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right'):
            context['self'].right(**pageargs)
        

        __M_writer('\r\n                </div>\r\n            </div>\r\n')
        __M_writer('            <div class="row">\r\n                <div class="col-sm-12" id="bottom">\r\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bottom'):
            context['self'].bottom(**pageargs)
        

        __M_writer('\r\n                </div>\r\n            </div>\r\n        </div>\r\n        <div id="loader-container">\r\n            <span id="loader"></span>\r\n            <p>LOADING ...</p>\r\n        </div>\r\n    </body>\r\n\r\n    <footer>\r\n        ')
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
{"filename": "C:/Users/hamcm/Desktop/S0/fomo/homepage/templates/base.htm", "uri": "homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "43": 2, "44": 9, "45": 9, "46": 9, "47": 12, "48": 12, "49": 12, "50": 13, "51": 13, "52": 14, "53": 14, "54": 15, "55": 15, "60": 16, "61": 18, "62": 21, "63": 22, "64": 22, "69": 28, "74": 33, "75": 38, "80": 40, "81": 44, "82": 46, "87": 47, "88": 50, "93": 51, "94": 54, "99": 55, "100": 59, "105": 61, "110": 72, "116": 16, "127": 28, "138": 33, "149": 40, "160": 47, "171": 51, "182": 55, "193": 61, "204": 72, "215": 204}}
__M_END_METADATA
"""

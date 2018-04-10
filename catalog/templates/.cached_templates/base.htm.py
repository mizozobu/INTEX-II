# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523314651.5424159
_enable_loop = True
_template_filename = '/mnt/c/Users/hilar/OneDrive - BYU Office 365/IS413/INTEX-II/catalog/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['header', 'top', 'center', 'maintenanceMessage', 'footer', 'right', 'addonlink', 'left', 'bottom']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def left():
            return render_left(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def top():
            return render_top(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def center():
            return render_center(context._locals(__M_locals))
        def bottom():
            return render_bottom(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        def right():
            return render_right(context._locals(__M_locals))
        def addonlink():
            return render_addonlink(context._locals(__M_locals))
        def maintenanceMessage():
            return render_maintenanceMessage(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <meta charset="UTF-8">\n    <head>\n        <title>FOMO</title>\n\n')
        __M_writer('        <link rel="icon" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/favicon.ico" type="image/x-icon"/>\n\n')
        __M_writer('        <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap/css/bootstrap-grid.min.css">\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap/css/bootstrap-grid.css">\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap/css/bootstrap.min.css">\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap/css/bootstrap.css">\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'addonlink'):
            context['self'].addonlink(**pageargs)
        

        __M_writer('\n')
        __M_writer('        <script src="http://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\n\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\n        ')
        __M_writer(str( django_mako_plus.links(self) ))
        __M_writer('\n    </head>\n    <body>\n        <div id="page">\n            <a class="d-none" href="#content">skip to content</a>\n            <div class="row">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'maintenanceMessage'):
            context['self'].maintenanceMessage(**pageargs)
        

        __M_writer('\n            </div>\n\n            <div class="row">\n                <div class="col-sm-12" id="header">\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\n                </div>\n            </div>\n\n')
        __M_writer('            <div class="row">\n                <div class="col-sm-12" id="top">\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        __M_writer('\n                </div>\n            </div>\n')
        __M_writer('            <div class="row">\n')
        __M_writer('                <div class="col-sm-2 d-none d-lg-block" id="left">\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\n                </div>\n')
        __M_writer('                <div class="col-sm-12 col-lg-8" id="center">\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer('\n                </div>\n')
        __M_writer('                <div class="col-sm-2 d-none d-lg-block" id="right">\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right'):
            context['self'].right(**pageargs)
        

        __M_writer('\n                </div>\n            </div>\n')
        __M_writer('            <div class="row">\n                <div class="col-sm-12" id="bottom">\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bottom'):
            context['self'].bottom(**pageargs)
        

        __M_writer('\n                </div>\n            </div>\n        </div>\n        <div id="loader-container">\n            <span id="loader"></span>\n            <p>LOADING ...</p>\n        </div>\n    </body>\n\n    <footer>\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\n    </footer>\n\n</html>\n')
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


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center():
            return render_center(context)
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


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
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


def render_addonlink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def addonlink():
            return render_addonlink(context)
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


def render_bottom(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bottom():
            return render_bottom(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/mnt/c/Users/hilar/OneDrive - BYU Office 365/IS413/INTEX-II/catalog/templates/base.htm", "uri": "base.htm", "line_map": {"64": 22, "149": 28, "171": 55, "69": 28, "193": 47, "74": 33, "75": 38, "204": 61, "138": 51, "80": 40, "81": 44, "18": 0, "215": 204, "110": 72, "87": 47, "88": 50, "100": 59, "93": 51, "94": 54, "182": 16, "160": 72, "99": 55, "82": 46, "105": 61, "43": 2, "44": 9, "45": 9, "46": 9, "47": 12, "48": 12, "49": 12, "50": 13, "51": 13, "52": 14, "53": 14, "54": 15, "55": 15, "116": 33, "127": 40, "60": 16, "61": 18, "62": 21, "63": 22}, "source_encoding": "utf-8"}
__M_END_METADATA
"""

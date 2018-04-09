# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1518311032.6805966
_enable_loop = True
_template_filename = 'C:/Users/hamcm/Desktop/s0/fomo/homepage/templates/ajax.html'
_template_uri = 'ajax.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['content', 'server_time']


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
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def server_time():
            return render_server_time(context._locals(__M_locals))
        now = context.get('now', UNDEFINED)
        st = context.get('st', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def server_time():
            return render_server_time(context)
        now = context.get('now', UNDEFINED)
        st = context.get('st', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h3>Congratulations -- you\'ve successfully created a new django-mako-plus app!</h3>\r\n      <h4>Next Up: Go through the django-mako-plus tutorial and add Javascript, CSS, and urlparams to this page.</h4>\r\n      <p class="server-time">\r\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'server_time'):
            context['self'].server_time(**pageargs)
        

        __M_writer('\r\n      </p>\r\n      <button id="server-time-button">Refresh Server Time</button>\r\n      <p class="browser-time">The current browser time is ')
        __M_writer(str( now ))
        __M_writer('.</p>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_server_time(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def server_time():
            return render_server_time(context)
        now = context.get('now', UNDEFINED)
        st = context.get('st', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n             The current server time is ')
        __M_writer(str( now ))
        __M_writer('.\r\n             ')
        __M_writer(str( st ))
        __M_writer('\r\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/hamcm/Desktop/s0/fomo/homepage/templates/ajax.html", "uri": "ajax.html", "source_encoding": "utf-8", "line_map": {"28": 0, "39": 1, "44": 16, "50": 3, "60": 3, "65": 11, "66": 14, "67": 14, "73": 8, "81": 8, "82": 9, "83": 9, "84": 10, "85": 10, "91": 85}}
__M_END_METADATA
"""

# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520123961.3756702
_enable_loop = True
_template_filename = 'C:/Users/hamcm/Desktop/S0/fomo/catalog/templates/demo.inner.html'
_template_uri = 'demo.inner.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('what?\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/hamcm/Desktop/S0/fomo/catalog/templates/demo.inner.html", "uri": "demo.inner.html", "source_encoding": "utf-8", "line_map": {"18": 0, "23": 1, "29": 23}}
__M_END_METADATA
"""

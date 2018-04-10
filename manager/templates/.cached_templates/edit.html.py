# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523403473.8590405
_enable_loop = True
_template_filename = 'C:/users/Scott Laptop/documents/Mariah/intex/intex-ii/manager/templates/edit.html'
_template_uri = 'edit.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['center']


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
    return runtime._inherit_from(context, 'manager/templates/app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        id = context.get('id', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def center():
            return render_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        id = context.get('id', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content top-buffer">\r\n        <div class="col-sm-6 col-centered">\r\n            <h1>Edit</h3>\r\n            <br />\r\n            <form action=')
        __M_writer(str( "/manager/edit/{}".format(id) ))
        __M_writer(' method="POST">\r\n                ')
        __M_writer(str( form ))
        __M_writer('\r\n            </form>\r\n            <br />\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/users/Scott Laptop/documents/Mariah/intex/intex-ii/manager/templates/edit.html", "uri": "edit.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "43": 14, "49": 3, "57": 3, "58": 8, "59": 8, "60": 9, "61": 9, "67": 61}}
__M_END_METADATA
"""

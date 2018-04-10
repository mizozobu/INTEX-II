# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523401961.3292596
_enable_loop = True
_template_filename = 'C:/users/Scott Laptop/documents/Mariah/intex/intex-ii/manager/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['center', 'left', 'right']


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
        def center():
            return render_center(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
        def left():
            return render_left(context._locals(__M_locals))
        def right():
            return render_right(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right'):
            context['self'].right(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center():
            return render_center(context)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content top-buffer">\r\n        <h1>All Products <a href=')
        __M_writer(str( "/manager/create/"))
        __M_writer(' class="btn btn-primary">Create New</a></h1>\r\n        <table class="table">\r\n            <tr>\r\n                <th>Category</th>\r\n                <th>Type</th>\r\n                <th>Name</th>\r\n                <th>Price</th>\r\n                <th>Quantity</th>\r\n                <th></th>\r\n                <th></th>\r\n            </tr>\r\n\r\n')
        for p in products:
            if p.status == '1':
                __M_writer('                <tr>\r\n                    <td>')
                __M_writer(str( p.category.name ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( p.__class__.__name__ ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( p.name ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( p.price ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( p.quantity ))
                __M_writer('</td>\r\n                    <td class="btn-holder">\r\n                        <a href=')
                __M_writer(str( "/manager/edit/{}".format(p.id) ))
                __M_writer(' class="btn btn-link">\r\n                          Edit\r\n                        </a>\r\n                    </td>\r\n                    <td>\r\n                      <a href=')
                __M_writer(str( "/manager/delete/{}".format(p.id) ))
                __M_writer(' class="btn btn-link">\r\n                        Delete\r\n                      </a>\r\n                    </td>\r\n                </tr>\r\n')
        __M_writer('\r\n        </table>\r\n    </div>\r\n')
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


def render_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right():
            return render_right(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/users/Scott Laptop/documents/Mariah/intex/intex-ii/manager/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "46": 41, "51": 43, "56": 45, "62": 3, "69": 3, "70": 5, "71": 5, "72": 17, "73": 18, "74": 19, "75": 20, "76": 20, "77": 21, "78": 21, "79": 22, "80": 22, "81": 23, "82": 23, "83": 24, "84": 24, "85": 26, "86": 26, "87": 31, "88": 31, "89": 38, "95": 43, "106": 45, "117": 106}}
__M_END_METADATA
"""

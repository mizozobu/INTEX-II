# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523500487.9905818
_enable_loop = True
_template_filename = 'C:/Users/Scott Laptop/Documents/Mariah/Intex/intex-ii/manager/templates/index.html'
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
        products = context.get('products', UNDEFINED)
        def left():
            return render_left(context._locals(__M_locals))
        def center():
            return render_center(context._locals(__M_locals))
        int = context.get('int', UNDEFINED)
        lowProducts = context.get('lowProducts', UNDEFINED)
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
        products = context.get('products', UNDEFINED)
        def center():
            return render_center(context)
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
        int = context.get('int', UNDEFINED)
        def left():
            return render_left(context)
        lowProducts = context.get('lowProducts', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <div class="content top-buffer">\r\n    <div id="reorderBox">\r\n      <h4>Low Inventory:</h4>\r\n      <hr>\r\n      <ul>\r\n')
        for item in lowProducts:
            __M_writer('            <li>')
            __M_writer(str( item.name ))
            __M_writer(' - ')
            __M_writer(str( int(item.quantity) ))
            __M_writer(' left</li>\r\n')
        __M_writer('      </ul>\r\n    </div>\r\n  </div>\r\n\r\n')
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
{"filename": "C:/Users/Scott Laptop/Documents/Mariah/Intex/intex-ii/manager/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "48": 41, "53": 56, "58": 58, "64": 3, "71": 3, "72": 5, "73": 5, "74": 17, "75": 18, "76": 19, "77": 20, "78": 20, "79": 21, "80": 21, "81": 22, "82": 22, "83": 23, "84": 23, "85": 24, "86": 24, "87": 26, "88": 26, "89": 31, "90": 31, "91": 38, "97": 43, "105": 43, "106": 49, "107": 50, "108": 50, "109": 50, "110": 50, "111": 50, "112": 52, "118": 58, "129": 118}}
__M_END_METADATA
"""

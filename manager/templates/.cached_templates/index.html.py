# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520126696.5808876
_enable_loop = True
_template_filename = 'C:/Users/hamcm/Desktop/S0/fomo/manager/templates/index.html'
_template_uri = 'index.html'
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
    return runtime._inherit_from(context, 'homepage/templates/app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def center():
            return render_center(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
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
        def center():
            return render_center(context)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <a href=')
        __M_writer(str( "/manager/create/"))
        __M_writer('><p class="btn btn-react">Create</p></a>\r\n        <table>\r\n            <tr>\r\n                <th></th>\r\n                <th>Category</th>\r\n                <th>Type</th>\r\n                <th>Name</th>\r\n                <th>Price</th>\r\n                <th>Quantity</th>\r\n                <th>Description</th>\r\n            </tr>\r\n\r\n')
        for p in products:
            if p.status == '1':
                __M_writer('                <tr>\r\n                    <td class="btn-holder">\r\n                        <a href=')
                __M_writer(str( "/manager/edit/{}".format(p.id) ))
                __M_writer('>\r\n                            <p class="btn btn-react-sm">Edit</p>\r\n                        </a>\r\n                        <a href=')
                __M_writer(str( "/manager/delete/{}".format(p.id) ))
                __M_writer('>\r\n                            <p class="btn btn-react-sm">Delete</p>\r\n                        </a>\r\n                    </td>\r\n                    <td>')
                __M_writer(str( p.category.name ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( p.__class__.__name__ ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( p.name ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( p.price ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( p.quantity ))
                __M_writer('</td>\r\n                    <td>')
                __M_writer(str( p.description ))
                __M_writer('</td>\r\n                </tr>\r\n')
        __M_writer('\r\n        </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/hamcm/Desktop/S0/fomo/manager/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "37": 1, "42": 40, "48": 3, "55": 3, "56": 5, "57": 5, "58": 17, "59": 18, "60": 19, "61": 21, "62": 21, "63": 24, "64": 24, "65": 28, "66": 28, "67": 29, "68": 29, "69": 30, "70": 30, "71": 31, "72": 31, "73": 32, "74": 32, "75": 33, "76": 33, "77": 37, "83": 77}}
__M_END_METADATA
"""

# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523333612.8083186
_enable_loop = True
_template_filename = 'C:/users/scott laptop/documents/mariah/intex/intex-ii/catalog/templates/thankyou.html'
_template_uri = 'thankyou.html'
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
    return runtime._inherit_from(context, 'catalog/templates/app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
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
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content text-center">\r\n        <h1>Thank You</h1>\r\n        <p id="message">\r\n          Your order is being processed, and will be shipped to you shortly.\r\n        </p>\r\n\r\n        <h3>Receipt</h3>\r\n\r\n        <p>You have ordered order.num_items() items.</p>\r\n        <p>The total price for your items is $ order.total_price.</p>\r\n\r\n        <br>\r\n\r\n        <a class="btn btn-default contShop" href="/catalog/">Continue Shopping</a>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/users/scott laptop/documents/mariah/intex/intex-ii/catalog/templates/thankyou.html", "uri": "thankyou.html", "source_encoding": "utf-8", "line_map": {"29": 0, "36": 1, "41": 19, "47": 3, "53": 3, "59": 53}}
__M_END_METADATA
"""

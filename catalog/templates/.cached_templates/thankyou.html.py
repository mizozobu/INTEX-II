# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523391538.786055
_enable_loop = True
_template_filename = 'C:/users/Scott Laptop/documents/Mariah/intex/intex-ii/catalog/templates/thankyou.html'
_template_uri = 'thankyou.html'
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
    return runtime._inherit_from(context, 'catalog/templates/app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        items = context.get('items', UNDEFINED)
        def left():
            return render_left(context._locals(__M_locals))
        def right():
            return render_right(context._locals(__M_locals))
        order = context.get('order', UNDEFINED)
        def center():
            return render_center(context._locals(__M_locals))
        tax = context.get('tax', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right'):
            context['self'].right(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        tax = context.get('tax', UNDEFINED)
        items = context.get('items', UNDEFINED)
        order = context.get('order', UNDEFINED)
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content text-center">\r\n        <h1>Thank You</h1>\r\n        <p id="message">\r\n          Your order is being processed, and will be shipped to you shortly.\r\n        </p>\r\n\r\n        <table class="table">\r\n          <thead>\r\n            <tr>\r\n              <th>Image</th>\r\n              <th>\r\n                Product\r\n              </th>\r\n              <th>\r\n                Quantity\r\n              </th>\r\n              <th>\r\n                Price\r\n              </th>\r\n              <th>\r\n                Item Total\r\n              </th>\r\n            </tr>\r\n          </thead>\r\n          <tbody>\r\n')
        for item in items:
            __M_writer('              <tr>\r\n                <td class="productTile">\r\n                    <img src="')
            __M_writer(str( item.product.image_url() ))
            __M_writer('" alt="Image of ')
            __M_writer(str( item.product.name ))
            __M_writer('" width="100px" />\r\n                </td>\r\n                <td>\r\n                  ')
            __M_writer(str( item.product.name ))
            __M_writer('\r\n                </td>\r\n                <td>\r\n                  ')
            __M_writer(str( item.quantity ))
            __M_writer('\r\n                </td>\r\n                <td>\r\n                  $')
            __M_writer(str( item.price))
            __M_writer(' each\r\n                </td>\r\n                <td>\r\n                  $')
            __M_writer(str( item.extended ))
            __M_writer('\r\n                </td>\r\n              </tr>\r\n')
        __M_writer('          </tbody>\r\n          <thead>\r\n            <tr>\r\n              <th>\r\n                Sales Tax:\r\n              </th>\r\n              <th>\r\n              </th>\r\n              <th>\r\n              </th>\r\n              <th>\r\n              </th>\r\n              <th>\r\n                $')
        __M_writer(str( tax.price ))
        __M_writer('\r\n              </th>\r\n            </tr>\r\n            <tr>\r\n              <th>\r\n                Total:\r\n              </th>\r\n              <th>\r\n              </th>\r\n              <th>\r\n              </th>\r\n              <th>\r\n              </th>\r\n              <th>\r\n                $')
        __M_writer(str( order.total_price ))
        __M_writer('\r\n              </th>\r\n            </tr>\r\n          </thead>\r\n        </table>\r\n\r\n        <a class="btn btn-primary contShop" href="/catalog/">Continue Shopping</a>\r\n    </div>\r\n')
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
{"filename": "C:/users/Scott Laptop/documents/Mariah/intex/intex-ii/catalog/templates/thankyou.html", "uri": "thankyou.html", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "48": 83, "53": 85, "58": 86, "64": 3, "73": 3, "74": 29, "75": 30, "76": 32, "77": 32, "78": 32, "79": 32, "80": 35, "81": 35, "82": 38, "83": 38, "84": 41, "85": 41, "86": 44, "87": 44, "88": 48, "89": 61, "90": 61, "91": 75, "92": 75, "98": 85, "109": 86, "120": 109}}
__M_END_METADATA
"""

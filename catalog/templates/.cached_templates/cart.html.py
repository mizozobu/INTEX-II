# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523394827.1335738
_enable_loop = True
_template_filename = 'C:/users/Scott Laptop/documents/Mariah/intex/intex-ii/catalog/templates/cart.html'
_template_uri = 'cart.html'
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
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def left():
            return render_left(context._locals(__M_locals))
        order = context.get('order', UNDEFINED)
        tax = context.get('tax', UNDEFINED)
        def right():
            return render_right(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
        def center():
            return render_center(context._locals(__M_locals))
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
        order = context.get('order', UNDEFINED)
        tax = context.get('tax', UNDEFINED)
        items = context.get('items', UNDEFINED)
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="content top-buffer bottom-buffer">\r\n  <h1>Shopping Cart <a class="btn btn-primary" href="/catalog/checkout/')
        __M_writer(str(order.id))
        __M_writer('">Checkout Now</a></h1>\r\n\r\n    <table class="table">\r\n      <thead>\r\n        <tr>\r\n          <th>Image</th>\r\n          <th>\r\n            Product\r\n          </th>\r\n          <th>\r\n            Quantity\r\n          </th>\r\n          <th>\r\n            Price\r\n          </th>\r\n          <th>\r\n            Item Total\r\n          </th>\r\n          <th>\r\n          </th>\r\n        </tr>\r\n      </thead>\r\n      <tbody>\r\n')
        for item in items:
            __M_writer('          <tr>\r\n            <td class="productTile spaceLeft">\r\n                <img src="')
            __M_writer(str( item.product.image_url() ))
            __M_writer('" alt="Image of ')
            __M_writer(str( item.product.name ))
            __M_writer('" width="100px" />\r\n            </td>\r\n            <td>\r\n              ')
            __M_writer(str( item.product.name ))
            __M_writer('\r\n            </td>\r\n            <td>\r\n              ')
            __M_writer(str( item.quantity ))
            __M_writer('\r\n            </td>\r\n            <td>\r\n              $')
            __M_writer(str( item.price))
            __M_writer(' each\r\n            </td>\r\n            <td>\r\n              $')
            __M_writer(str( item.extended ))
            __M_writer('\r\n            </td>\r\n            <td class="spaceRight">\r\n              <a href="/catalog/delete/')
            __M_writer(str(item.id))
            __M_writer('/')
            __M_writer(str(order.id))
            __M_writer('">Delete</a>\r\n            </td>\r\n          </tr>\r\n')
        __M_writer('      </tbody>\r\n      <thead>\r\n        <tr>\r\n          <th class="spaceLeft">\r\n            Sales Tax:\r\n          </th>\r\n          <th>\r\n          </th>\r\n          <th>\r\n          </th>\r\n          <th>\r\n          </th>\r\n          <th>\r\n            $')
        __M_writer(str( tax.price ))
        __M_writer('\r\n          </th>\r\n          <th>\r\n          </th>\r\n        </tr>\r\n        <tr>\r\n          <th>\r\n            Total:\r\n          </th>\r\n          <th>\r\n          </th>\r\n          <th>\r\n          </th>\r\n          <th>\r\n          </th>\r\n          <th>\r\n            $')
        __M_writer(str( order.total_price ))
        __M_writer('\r\n          </th>\r\n          <th>\r\n          </th>\r\n        </tr>\r\n      </thead>\r\n    </table>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right():
            return render_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/users/Scott Laptop/documents/Mariah/intex/intex-ii/catalog/templates/cart.html", "uri": "cart.html", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "48": 87, "53": 90, "58": 92, "64": 3, "73": 3, "74": 5, "75": 5, "76": 28, "77": 29, "78": 31, "79": 31, "80": 31, "81": 31, "82": 34, "83": 34, "84": 37, "85": 37, "86": 40, "87": 40, "88": 43, "89": 43, "90": 46, "91": 46, "92": 46, "93": 46, "94": 50, "95": 63, "96": 63, "97": 79, "98": 79, "104": 89, "110": 89, "116": 91, "122": 91, "128": 122}}
__M_END_METADATA
"""

# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523314651.488104
_enable_loop = True
_template_filename = '/mnt/c/Users/hilar/OneDrive - BYU Office 365/IS413/INTEX-II/catalog/templates/cart.html'
_template_uri = 'cart.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['left', 'top', 'center', 'right']


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
        def top():
            return render_top(context._locals(__M_locals))
        def center():
            return render_center(context._locals(__M_locals))
        tax = context.get('tax', UNDEFINED)
        def right():
            return render_right(context._locals(__M_locals))
        def left():
            return render_left(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
        order = context.get('order', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right'):
            context['self'].right(**pageargs)
        

        __M_writer('\r\n')
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


def render_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top():
            return render_top(context)
        __M_writer = context.writer()
        __M_writer('<h1>Cart</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        tax = context.get('tax', UNDEFINED)
        items = context.get('items', UNDEFINED)
        def center():
            return render_center(context)
        order = context.get('order', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <table class="table">\r\n    <thead>\r\n      <tr>\r\n        <th>\r\n          Product\r\n        </th>\r\n        <th>\r\n          Quantity\r\n        </th>\r\n        <th>\r\n          Price\r\n        </th>\r\n        <th>\r\n          Item Total\r\n        </th>\r\n        <th>\r\n        </th>\r\n      </tr>\r\n    </thead>\r\n    <tbody>\r\n')
        for item in items:
            __M_writer('        <tr>\r\n          <td>\r\n            ')
            __M_writer(str( item.product.name ))
            __M_writer('\r\n          </td>\r\n          <td>\r\n            ')
            __M_writer(str( item.quantity ))
            __M_writer('\r\n          </td>\r\n          <td>\r\n            ')
            __M_writer(str( item.price))
            __M_writer(' each\r\n          </td>\r\n          <td>\r\n            ')
            __M_writer(str( item.extended ))
            __M_writer('\r\n          </td>\r\n          <td>\r\n            <a href="/catalog/delete/')
            __M_writer(str(item.id))
            __M_writer('/')
            __M_writer(str(order.id))
            __M_writer('">Delete</a>\r\n          </td>\r\n        </tr>\r\n')
        __M_writer('    </tbody>\r\n    <thead>\r\n      <tr>\r\n        <th>\r\n          Sales Tax:\r\n        </th>\r\n        <th>\r\n        </th>\r\n        <th>\r\n        </th>\r\n        <th>\r\n          ')
        __M_writer(str( tax.price ))
        __M_writer('\r\n        </th>\r\n        <th>\r\n        </th>\r\n      </tr>\r\n      <tr>\r\n        <th>\r\n          Total:\r\n        </th>\r\n        <th>\r\n        </th>\r\n        <th>\r\n        </th>\r\n        <th>\r\n          ')
        __M_writer(str( order.total_price ))
        __M_writer('\r\n        </th>\r\n        <th>\r\n        </th>\r\n      </tr>\r\n    </thead>\r\n  </table>\r\n  <a class="btn btn-default" href="/catalog/checkout/')
        __M_writer(str(order.id))
        __M_writer('">Checkout Now</a>\r\n')
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
{"filename": "/mnt/c/Users/hilar/OneDrive - BYU Office 365/IS413/INTEX-II/catalog/templates/cart.html", "uri": "cart.html", "line_map": {"65": 80, "130": 80, "71": 79, "119": 56, "141": 130, "109": 32, "124": 77, "82": 3, "88": 3, "29": 0, "94": 5, "114": 41, "103": 5, "104": 26, "105": 27, "106": 29, "107": 29, "108": 32, "45": 1, "110": 35, "111": 35, "112": 38, "113": 38, "50": 3, "115": 41, "116": 41, "117": 41, "118": 45, "55": 78, "120": 56, "121": 70, "122": 70, "123": 77, "60": 79}, "source_encoding": "utf-8"}
__M_END_METADATA
"""

# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523332685.2152507
_enable_loop = True
_template_filename = 'C:/users/scott laptop/documents/mariah/intex/intex-ii/catalog/templates/checkout.html'
_template_uri = 'checkout.html'
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
    ns = runtime.ModuleNamespace('fl', context._clean_inheritance_tokens(), callables=None, calling_uri=_template_uri, module='formlib.tags')
    context.namespaces[(__name__, 'fl')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'catalog/templates/app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        order = context.get('order', UNDEFINED)
        fl = _mako_get_namespace(context, 'fl')
        def center():
            return render_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
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
        order = context.get('order', UNDEFINED)
        fl = _mako_get_namespace(context, 'fl')
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="content">\r\n<h1>You are about to pay $')
        __M_writer(str(order.total_price))
        __M_writer('.</h1>\r\n<p>Please enter your shipping information below.</p>\r\n  <div id="form">\r\n    ')
        def ccall(caller):
            def body():
                settings = context.get('settings', UNDEFINED)
                __M_writer = context.writer()
                __M_writer('\r\n      <div class="text-center">\r\n        <script\r\n          src="https://checkout.stripe.com/checkout.js"\r\n          class="stripe-button"\r\n          data-key="')
                __M_writer(str(settings.STRIPE_PUBLIC_KEY))
                __M_writer('"\r\n          data-amount="')
                __M_writer(str(order.total_price * 100))
                __M_writer('"\r\n          data-name="FOMO"\r\n          data-description="Widget"\r\n          data-image="https://stripe.com/img/documentation/checkout/marketplace.png"\r\n          data-locale="auto"\r\n          data-label="Pay Now">\r\n        </script>\r\n      </div>\r\n    ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(str(fl.render()))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer('\r\n  </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/users/scott laptop/documents/mariah/intex/intex-ii/catalog/templates/checkout.html", "uri": "checkout.html", "source_encoding": "utf-8", "line_map": {"25": 2, "31": 0, "40": 1, "41": 2, "46": 26, "52": 4, "60": 4, "61": 6, "62": 6, "67": 9, "68": 14, "69": 14, "70": 15, "71": 15, "76": 9, "79": 23, "85": 79}}
__M_END_METADATA
"""

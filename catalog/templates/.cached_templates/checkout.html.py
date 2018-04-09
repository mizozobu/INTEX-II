# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523064306.9914093
_enable_loop = True
_template_filename = 'C:/Users/hamcm/Desktop/S0/fomo/catalog/templates/checkout.html'
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
        fl = _mako_get_namespace(context, 'fl')
        form = context.get('form', UNDEFINED)
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
        fl = _mako_get_namespace(context, 'fl')
        form = context.get('form', UNDEFINED)
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        ')
        __M_writer(str( form ))
        __M_writer('\r\n        ')
        def ccall(caller):
            def body():
                settings = context.get('settings', UNDEFINED)
                __M_writer = context.writer()
                __M_writer('\r\n            <div class="text-center">\r\n                <script\r\n                    src="https://checkout.stripe.com/checkout.js"\r\n                    class="stripe-button"\r\n                    data-key="')
                __M_writer(str(settings.STRIPE_PUBLIC_KEY))
                __M_writer('"\r\n                    data-amount="999"\r\n                    data-name="FOMO"\r\n                    data-description="Widget"\r\n                    data-image="https://stripe.com/img/documentation/checkout/marketplace.png"\r\n                    data-locale="auto"\r\n                    data-label="Pay Now">\r\n                </script>\r\n            </div>\r\n        ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(str(fl.render()))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer('\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/hamcm/Desktop/S0/fomo/catalog/templates/checkout.html", "uri": "checkout.html", "source_encoding": "utf-8", "line_map": {"25": 2, "31": 0, "40": 1, "41": 2, "46": 23, "52": 4, "60": 4, "61": 6, "62": 6, "67": 7, "68": 12, "69": 12, "74": 7, "77": 21, "83": 77}}
__M_END_METADATA
"""

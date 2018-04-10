# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523319846.9632878
_enable_loop = True
_template_filename = '/mnt/c/Users/hilar/OneDrive - BYU Office 365/IS413/INTEX-II/catalog/templates/checkout.html'
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
        def center():
            return render_center(context._locals(__M_locals))
        order = context.get('order', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        fl = _mako_get_namespace(context, 'fl')
        def center():
            return render_center(context)
        order = context.get('order', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<h1>You are about to pay $')
        __M_writer(str(order.total_price))
        __M_writer('</h1>\n  <div id="form">\n    ')
        def ccall(caller):
            def body():
                settings = context.get('settings', UNDEFINED)
                __M_writer = context.writer()
                __M_writer('\n      <div class="text-center">\n        <script\n          src="https://checkout.stripe.com/checkout.js"\n          class="stripe-button"\n          data-key="')
                __M_writer(str(settings.STRIPE_PUBLIC_KEY))
                __M_writer('"\n          data-amount="')
                __M_writer(str(order.total_price * 100))
                __M_writer('"\n          data-name="FOMO"\n          data-description="Widget"\n          data-image="https://stripe.com/img/documentation/checkout/marketplace.png"\n          data-locale="auto"\n          data-label="Pay Now">\n        </script>\n      </div>\n    ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(str(fl.render()))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer('\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"67": 7, "68": 12, "69": 12, "70": 13, "71": 13, "40": 1, "41": 2, "76": 7, "46": 23, "79": 21, "52": 4, "85": 79, "25": 2, "60": 4, "61": 5, "62": 5, "31": 0}, "uri": "checkout.html", "source_encoding": "utf-8", "filename": "/mnt/c/Users/hilar/OneDrive - BYU Office 365/IS413/INTEX-II/catalog/templates/checkout.html"}
__M_END_METADATA
"""

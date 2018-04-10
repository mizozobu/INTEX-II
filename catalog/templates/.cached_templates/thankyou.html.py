# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523317271.6751156
_enable_loop = True
_template_filename = '/mnt/c/Users/hilar/OneDrive - BYU Office 365/IS413/INTEX-II/catalog/templates/thankyou.html'
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
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="content">\n        <h1>Thank You</h1>\n        <p id="message">\n          Your order is being processed, and will be shipped to you shortly.\n\n        </p>\n        <a class="btn btn-default contShop" href="/catalog/">Continue Shopping</a>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"36": 1, "53": 3, "41": 12, "59": 53, "29": 0, "47": 3}, "uri": "thankyou.html", "filename": "/mnt/c/Users/hilar/OneDrive - BYU Office 365/IS413/INTEX-II/catalog/templates/thankyou.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""

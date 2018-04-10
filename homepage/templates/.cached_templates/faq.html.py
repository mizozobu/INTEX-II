# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523332245.5800705
_enable_loop = True
_template_filename = 'C:/users/scott laptop/documents/mariah/intex/intex-ii/homepage/templates/faq.html'
_template_uri = 'faq.html'
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
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
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
        __M_writer('\r\n      <h2>Frequently Asked Questions</h3>\r\n        <br>\r\n\r\n        <h4 class="top-buffer"><strong>How does your rent-to-own program work?</strong></h6>\r\n          <p>With the rent-to-own program, the first eight months of rent go 100% toward the purchase price if the renter chooses to buy at that point. Any rent beyond the first eight months only counts 50% toward the purchase price. All renters are assumed to be rent-to-own until they physically return the instrument. Even if the renter doesn’t indicate a rent-to-own preference, If they pay rent sufficient to cover the instrument cost, the instrument is then considered sold.</p>\r\n\r\n        <hr>\r\n\r\n        <h4 class="top-buffer"><strong>Can I get my instrument repaired here?</strong></h6>\r\n          <p>We do have a repair shop in the building that allows a wide variety of instruments to be repaired or reconditioned. An estimate is calculated before any repairs are started. However, payment isn’t due until the repair is complete. If the repair is beyond the capabilities at our store, we have preferred partners we recommend the instrument owners use.</p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/users/scott laptop/documents/mariah/intex/intex-ii/homepage/templates/faq.html", "uri": "faq.html", "source_encoding": "utf-8", "line_map": {"29": 0, "36": 1, "41": 14, "47": 3, "53": 3, "59": 53}}
__M_END_METADATA
"""

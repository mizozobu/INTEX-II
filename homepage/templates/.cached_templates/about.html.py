# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520126506.24467
_enable_loop = True
_template_filename = 'C:/Users/hamcm/Desktop/S0/fomo/homepage/templates/about.html'
_template_uri = 'about.html'
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
        __M_writer('\r\n    <div class="content">\r\n        <h3>About us</h3>\r\n        <h4>FOMO is uber awesome music store just for you!</h4>\r\n        <br />\r\n        <p>Accesibilitty Improvement</p>\r\n        <ul>\r\n            <li>color change</li>\r\n            <li>anchor link to skip to content</li>\r\n            <li>alt text added for images</li>\r\n            <li>Use of hierarchical headings in order</li>\r\n        </ul>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/hamcm/Desktop/S0/fomo/homepage/templates/about.html", "uri": "about.html", "source_encoding": "utf-8", "line_map": {"29": 0, "36": 1, "41": 16, "47": 3, "53": 3, "59": 53}}
__M_END_METADATA
"""
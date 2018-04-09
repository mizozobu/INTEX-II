# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523309462.040168
_enable_loop = True
_template_filename = 'C:/INTEX-II-hilarySprint7/catalog/templates/detail.html'
_template_uri = 'detail.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['center']


from catalog import models as m 

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
        product = context.get('product', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer('\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center():
            return render_center(context)
        product = context.get('product', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    \r\n<div class="content">\n        <div class="container">\n         \r\n   <ul class="product-images">\n                \r\n')
        for url in product.image_urls():
            __M_writer('                  \r\n\r\n  <li class="small-image"><img src="')
            __M_writer(str(url))
            __M_writer('" alt=')
            __M_writer(str(product.name))
            __M_writer('>\r\n</li>\n')
        __M_writer('            </ul>\n            \r\n<img class="big-image" src="')
        __M_writer(str(product.image_url()))
        __M_writer('" alt=')
        __M_writer(str(product.name))
        __M_writer('>\n           \r\n <h1>')
        __M_writer(str(product.name))
        __M_writer('</h1>\n            <p>')
        __M_writer(str(product.description))
        __M_writer('</p>\n         \r\n   <div class="action">\n             \r\n<div id="form">\n                  ')
        __M_writer(str( form ))
        __M_writer('\n          \r\n    </div>\n                <!-- <form action="">\n                \r\n                       <input type="submit" class="btn btn-react-white" value="Purchase" />\n                </form> -->\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/INTEX-II-hilarySprint7/catalog/templates/detail.html", "uri": "detail.html", "source_encoding": "utf-8", "line_map": {"18": 3, "31": 0, "40": 1, "41": 3, "46": 38, "52": 5, "60": 5, "61": 12, "62": 13, "63": 15, "64": 15, "65": 15, "66": 15, "67": 18, "68": 20, "69": 20, "70": 20, "71": 20, "72": 22, "73": 22, "74": 23, "75": 23, "76": 28, "77": 28, "83": 77}}
__M_END_METADATA
"""

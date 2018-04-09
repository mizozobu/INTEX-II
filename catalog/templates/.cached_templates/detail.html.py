# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1521518637.1512558
_enable_loop = True
_template_filename = 'C:/Users/hamcm/Desktop/S0/fomo/catalog/templates/detail.html'
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
        range = context.get('range', UNDEFINED)
        product = context.get('product', UNDEFINED)
        type = context.get('type', UNDEFINED)
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
        def center():
            return render_center(context)
        range = context.get('range', UNDEFINED)
        product = context.get('product', UNDEFINED)
        type = context.get('type', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <div class="container">\r\n            <ul class="product-images">\r\n')
        for url in product.image_urls():
            __M_writer('                    <li class="small-image"><img src="')
            __M_writer(str(url))
            __M_writer('" alt=')
            __M_writer(str(product.name))
            __M_writer('></li>\r\n')
        __M_writer('            </ul>\r\n            <img class="big-image" src="')
        __M_writer(str(product.image_url()))
        __M_writer('" alt=')
        __M_writer(str(product.name))
        __M_writer('>\r\n            <h1>')
        __M_writer(str(product.name))
        __M_writer('</h1>\r\n            <p>')
        __M_writer(str(product.description))
        __M_writer('</p>\r\n            <div class="action">\r\n                <form action="">\r\n')
        if type(product) is m.BulkProduct:
            __M_writer('                    <select name="quantity">\r\n')
            for n in range(5):
                __M_writer('                            <option value="')
                __M_writer(str(n+1))
                __M_writer('">')
                __M_writer(str(n+1))
                __M_writer('</option>\r\n')
            __M_writer('                        <br><br>\r\n                    </select>\r\n')
        __M_writer('                    <input type="submit" class="btn btn-react-white" value="Purchase" />\r\n                </form>\r\n            </div>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/hamcm/Desktop/S0/fomo/catalog/templates/detail.html", "uri": "detail.html", "source_encoding": "utf-8", "line_map": {"18": 2, "31": 0, "41": 1, "42": 2, "47": 30, "53": 4, "62": 4, "63": 8, "64": 9, "65": 9, "66": 9, "67": 9, "68": 9, "69": 11, "70": 12, "71": 12, "72": 12, "73": 12, "74": 13, "75": 13, "76": 14, "77": 14, "78": 17, "79": 18, "80": 19, "81": 20, "82": 20, "83": 20, "84": 20, "85": 20, "86": 22, "87": 25, "93": 87}}
__M_END_METADATA
"""

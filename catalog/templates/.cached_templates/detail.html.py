# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523311859.5002463
_enable_loop = True
_template_filename = '/mnt/c/Users/hilar/OneDrive - BYU Office 365/IS413/INTEX-II/catalog/templates/detail.html'
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
        product = context.get('product', UNDEFINED)
        type = context.get('type', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def center():
            return render_center(context._locals(__M_locals))
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer('\n\n\n<!-- <form action="">\n')
        if type(product) is m.BulkProduct:
            __M_writer('    <select name="quantity">\n')
            for n in range(5):
                __M_writer('            <option value="')
                __M_writer(str(n+1))
                __M_writer('">')
                __M_writer(str(n+1))
                __M_writer('</option>\n')
            __M_writer('        <br><br>\n    </select>\n')
        __M_writer('    <input type="submit" class="btn btn-react-white" value="Purchase" />\n</form> -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        product = context.get('product', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="content">\n        <div class="container">\n            <ul class="product-images">\n')
        for url in product.image_urls():
            __M_writer('                    <li class="small-image"><img src="')
            __M_writer(str(url))
            __M_writer('" alt=')
            __M_writer(str(product.name))
            __M_writer('></li>\n')
        __M_writer('            </ul>\n            <img class="big-image" src="')
        __M_writer(str(product.image_url()))
        __M_writer('" alt=')
        __M_writer(str(product.name))
        __M_writer('>\n            <h1>')
        __M_writer(str(product.name))
        __M_writer('</h1>\n            <p>')
        __M_writer(str(product.description))
        __M_writer('</p>\n            <div class="action">\n                ')
        __M_writer(str( form ))
        __M_writer('\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 4, "72": 4, "73": 8, "74": 9, "75": 9, "76": 9, "77": 9, "78": 9, "79": 11, "80": 12, "81": 12, "18": 2, "83": 12, "84": 13, "85": 13, "86": 14, "87": 14, "88": 16, "89": 16, "31": 0, "42": 1, "43": 2, "82": 12, "48": 20, "49": 24, "50": 25, "51": 26, "52": 27, "53": 27, "54": 27, "55": 27, "56": 27, "57": 29, "58": 32, "95": 89}, "uri": "detail.html", "source_encoding": "utf-8", "filename": "/mnt/c/Users/hilar/OneDrive - BYU Office 365/IS413/INTEX-II/catalog/templates/detail.html"}
__M_END_METADATA
"""

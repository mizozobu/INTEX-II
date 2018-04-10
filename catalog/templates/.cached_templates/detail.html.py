# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523393387.7203586
_enable_loop = True
_template_filename = 'C:/users/Scott Laptop/documents/Mariah/intex/intex-ii/catalog/templates/detail.html'
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
        type = context.get('type', UNDEFINED)
        form = context.get('form', UNDEFINED)
        product = context.get('product', UNDEFINED)
        int = context.get('int', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer('\r\n\r\n\r\n<!-- <form action="">\r\n')
        if type(product) is m.BulkProduct:
            __M_writer('    <select name="quantity">\r\n')
            for n in range(5):
                __M_writer('            <option value="')
                __M_writer(str(n+1))
                __M_writer('">')
                __M_writer(str(n+1))
                __M_writer('</option>\r\n')
            __M_writer('        <br><br>\r\n    </select>\r\n')
        __M_writer('    <input type="submit" class="btn btn-react-white" value="Purchase" />\r\n</form> -->\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center():
            return render_center(context)
        product = context.get('product', UNDEFINED)
        int = context.get('int', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="content">\r\n    <div class="container">\r\n      <div class="productTile">\r\n        <ul class="product-images">\r\n')
        for url in product.image_urls():
            __M_writer('                <li class="small-image"><img src="')
            __M_writer(str(url))
            __M_writer('" alt=')
            __M_writer(str(product.name))
            __M_writer('></li>\r\n')
        __M_writer('        </ul>\r\n          <img class="big-image" src="')
        __M_writer(str(product.image_url()))
        __M_writer('" alt=')
        __M_writer(str(product.name))
        __M_writer('>\r\n      </div>\r\n\r\n      <div>\r\n        <h1>')
        __M_writer(str(product.name))
        __M_writer('</h1>\r\n        <p>')
        __M_writer(str(product.description))
        __M_writer('</p>\r\n        <p>Quantity Remaining: ')
        __M_writer(str( int(product.quantity) ))
        __M_writer('\r\n      </div>\r\n\r\n      <div class="action">\r\n          ')
        __M_writer(str( form ))
        __M_writer('\r\n      </div>\r\n    </div>\r\n</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/users/Scott Laptop/documents/Mariah/intex/intex-ii/catalog/templates/detail.html", "uri": "detail.html", "source_encoding": "utf-8", "line_map": {"18": 2, "31": 0, "43": 1, "44": 2, "49": 29, "50": 33, "51": 34, "52": 35, "53": 36, "54": 36, "55": 36, "56": 36, "57": 36, "58": 38, "59": 41, "65": 4, "74": 4, "75": 10, "76": 11, "77": 11, "78": 11, "79": 11, "80": 11, "81": 13, "82": 14, "83": 14, "84": 14, "85": 14, "86": 18, "87": 18, "88": 19, "89": 19, "90": 20, "91": 20, "92": 24, "93": 24, "99": 93}}
__M_END_METADATA
"""

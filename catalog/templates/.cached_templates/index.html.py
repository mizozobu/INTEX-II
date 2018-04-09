# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1521329013.81483
_enable_loop = True
_template_filename = 'C:/Users/hamcm/Desktop/S0/fomo/catalog/templates/index.html'
_template_uri = 'index.html'
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
        products = context.get('products', UNDEFINED)
        num_pages = context.get('num_pages', UNDEFINED)
        def center():
            return render_center(context._locals(__M_locals))
        page = context.get('page', UNDEFINED)
        category_name = context.get('category_name', UNDEFINED)
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
        products = context.get('products', UNDEFINED)
        num_pages = context.get('num_pages', UNDEFINED)
        def center():
            return render_center(context)
        page = context.get('page', UNDEFINED)
        category_name = context.get('category_name', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <div class="page-navigator">\r\n')
        if category_name != "Products":
            __M_writer('                <h1 class="category">')
            __M_writer(str(category_name))
            __M_writer('</h1>\r\n')
        else:
            __M_writer('                <h1 class="category">Products</h1>\r\n')
        __M_writer('            <p>\r\n                <span id="pagenator">\r\n                    <span id="left-arrow" class="arrow"> &blacktriangleleft; </span>\r\n                    <span id="page_text">Page <span id="current-page">')
        __M_writer(str(page))
        __M_writer('</span> / <span id="last-page">')
        __M_writer(str(num_pages))
        __M_writer('</span></span>\r\n                    <span id="right-arrow" class="arrow"> &blacktriangleright; </span>\r\n                </span>\r\n            </p>\r\n        </div>\r\n        <div id="products">\r\n            <ul class="catalog">\r\n')
        for p in products:
            if p.status == '1':
                __M_writer('                        <a href="/catalog/detail/')
                __M_writer(str(p.id))
                __M_writer('"><li class="product">\r\n                            <div class="price">&dollar;')
                __M_writer(str(p.price))
                __M_writer('</div>\r\n                            <div class="name"><p>')
                __M_writer(str(p.name))
                __M_writer('</p></div>\r\n                            <img src="')
                __M_writer(str(p.image_url()))
                __M_writer('" alt=')
                __M_writer(str(p.name))
                __M_writer('>\r\n                            <div class="cover-container">\r\n                                <div class="cover">\r\n                                    <div class="cover-name"><p>')
                __M_writer(str(p.name))
                __M_writer('</p></div>\r\n                                    <div class="cover-price">&dollar;')
                __M_writer(str(p.price))
                __M_writer('</div>\r\n                                </div>\r\n                            </div>\r\n                        </li></a>\r\n')
        __M_writer('            </ul>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/hamcm/Desktop/S0/fomo/catalog/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "45": 39, "51": 3, "61": 3, "62": 6, "63": 7, "64": 7, "65": 7, "66": 8, "67": 9, "68": 11, "69": 14, "70": 14, "71": 14, "72": 14, "73": 21, "74": 22, "75": 23, "76": 23, "77": 23, "78": 24, "79": 24, "80": 25, "81": 25, "82": 26, "83": 26, "84": 26, "85": 26, "86": 29, "87": 29, "88": 30, "89": 30, "90": 36, "96": 90}}
__M_END_METADATA
"""

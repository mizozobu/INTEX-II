# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523398572.0555804
_enable_loop = True
_template_filename = 'C:/users/Scott Laptop/documents/Mariah/intex/intex-ii/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['addonlink', 'top']


from catalog import models as cmod 

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
        def top():
            return render_top(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def addonlink():
            return render_addonlink(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'addonlink'):
            context['self'].addonlink(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_addonlink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def addonlink():
            return render_addonlink(context)
        __M_writer = context.writer()
        __M_writer("\r\n<link href='http://fonts.googleapis.com/css?family=Oleo+Script' rel='stylesheet' type='text/css'>\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top():
            return render_top(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="content">\r\n    <div class="row" id="eye-catcher">\r\n        <div class="col-md-6 text-center">\r\n            <h1 id="head-text"><strong><span id="row-1">Family Oriented</span><br /><span id="row-2">Music Organization</span></strong></h1>\r\n            <a href="#content"><p class="btn btn-md" id="btn-explore">SHOP &raquo;</p></a>\r\n        </div>\r\n        <div class="col-md-6">\r\n            <div class="grid-container-img">\r\n                <div class="grid-item layer1 r-1 c-4"><img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('catalog/media/instruments/violin.jpg" alt="violin" /></div>\r\n                <div class="grid-item layer1 r-1 c-5"><img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('catalog/media/instruments/drum.jpg" alt="drum" /></div>\r\n                <div class="grid-item layer2 r-1 c-6"><img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('catalog/media/instruments/trumpet.jpg" alt="trumpet" /></div>\r\n                <div class="grid-item layer2 r-2 c-4"><img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('catalog/media/instruments/piano.jpg" alt="piano" /></div>\r\n                <div class="grid-item layer1 r-2 c-5"><img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('catalog/media/instruments/fluto.jpg" alt="fluto" /></div>\r\n                <div class="grid-item layer1 r-2 c-6"><img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('catalog/media/instruments/gitar.jpg" alt="gitar" /></div>\r\n                <div class="grid-item layer1 r-3 c-4"><img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('catalog/media/instruments/synthesizer.jpg" alt="synthesizer" /></div>\r\n                <div class="grid-item layer2 r-3 c-5"><img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('catalog/media/instruments/malimba.jpg" alt="malimba" /></div>\r\n                <div class="grid-item layer2 r-3 c-6"><img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('catalog/media/instruments/oboe.jpg" alt="oboe" /></div>\r\n            </div>\r\n        </div>\r\n    </div>\r\n    <div class="row background-white" id="content">\r\n        <div class="grid-container-jt">\r\n\r\n          ')
        softId = cmod.Category.objects.get(name='Software').id 
        
        __M_writer('\r\n\r\n            <a href="/catalog/index/')
        __M_writer(str( softId ))
        __M_writer('">\r\n              <div class="grid-item">\r\n                <div class="jumbotron">\r\n                    <h2 class="display-4">Software</h2>\r\n                    <hr class="my-4">\r\n                    <p class="lead">We have a wide selection of tools for you to use in your musical pursuits.</p>\r\n                </div>\r\n              </div>\r\n            </a>\r\n\r\n            ')
        instId = cmod.Category.objects.get(name='Instruments').id 
        
        __M_writer('\r\n\r\n            <a href="/catalog/index/')
        __M_writer(str( instId ))
        __M_writer('">\r\n              <div class="grid-item">\r\n                <div class="jumbotron">\r\n                    <h2 class="display-4">Instruments</h2>\r\n                    <hr class="my-4">\r\n                    <p class="lead">View our selection of instruments that you can rent or buy.</p>\r\n                </div>\r\n              </div>\r\n            </a>\r\n\r\n            <a href="/catalog/index/"><div class="grid-item">\r\n                <div class="jumbotron">\r\n                    <h2 class="display-4">And More!</h2>\r\n                    <hr class="my-4">\r\n                    <p class="lead">View our assortment of other tools and products available for you.</p>\r\n                </div>\r\n            </div>\r\n          </a>\r\n\r\n        </div>\r\n    </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/users/Scott Laptop/documents/Mariah/intex/intex-ii/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"18": 2, "31": 0, "41": 1, "42": 2, "47": 6, "52": 68, "58": 4, "64": 4, "70": 8, "77": 8, "78": 17, "79": 17, "80": 18, "81": 18, "82": 19, "83": 19, "84": 20, "85": 20, "86": 21, "87": 21, "88": 22, "89": 22, "90": 23, "91": 23, "92": 24, "93": 24, "94": 25, "95": 25, "96": 32, "98": 32, "99": 34, "100": 34, "101": 44, "103": 44, "104": 46, "105": 46, "111": 105}}
__M_END_METADATA
"""

# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520133389.744194
_enable_loop = True
_template_filename = 'C:/Users/hamcm/Desktop/S0/fomo/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['addonlink', 'top']


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
        def addonlink():
            return render_addonlink(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
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
        __M_writer('catalog/media/instruments/oboe.jpg" alt="oboe" /></div>\r\n            </div>\r\n        </div>\r\n    </div>\r\n    <div class="row background-white" id="content">\r\n        <div class="grid-container-jt">\r\n            <a href="/catalog/"><div class="grid-item">\r\n                <div class="jumbotron">\r\n                    <h2 class="display-4">Signiture Instrument</h2>\r\n                    <hr class="my-4">\r\n                    <p class="lead">Our signiture insturment is made by craftsman. Find one and only instrument for you.</p>\r\n                </div>\r\n            </div></a>\r\n            <a href="/catalog/"><div class="grid-item">\r\n                <div class="jumbotron">\r\n                    <h2 class="display-4">Renal Instrument</h2>\r\n                    <hr class="my-4">\r\n                    <p class="lead">Just looking for an instrument for a short period of time? Don\'t worry. We don\'t make you buy one.</p>\r\n                </div>\r\n            </div></a>\r\n            <a href="/catalog/"><div class="grid-item">\r\n                <div class="jumbotron">\r\n                    <h2 class="display-4">Equipments</h2>\r\n                    <hr class="my-4">\r\n                    <p class="lead">Parts, tools, sheet music, varnish, and anything that enhances your music life.</p>\r\n                </div>\r\n            </div></a>\r\n        </div>\r\n    </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/hamcm/Desktop/S0/fomo/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "39": 1, "44": 5, "49": 54, "55": 3, "61": 3, "67": 7, "74": 7, "75": 16, "76": 16, "77": 17, "78": 17, "79": 18, "80": 18, "81": 19, "82": 19, "83": 20, "84": 20, "85": 21, "86": 21, "87": 22, "88": 22, "89": 23, "90": 23, "91": 24, "92": 24, "98": 92}}
__M_END_METADATA
"""

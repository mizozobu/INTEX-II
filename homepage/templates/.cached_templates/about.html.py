# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523330384.6293757
_enable_loop = True
_template_filename = 'C:/users/scott laptop/documents/mariah/intex/intex-ii/homepage/templates/about.html'
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
        __M_writer('\r\n\r\n\r\n')
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
        __M_writer('\r\n    <h3>The Family Oriented Music Organization</h3>\r\n    <p>The Family Oriented Music Organization, otherwise known as FOMO, is a family owned music store that’s been operating in Utah Valley since 1952. We are dedicated to helping provide quality instruments to musicians of all skill levels. We have seen the benefits of music in our own personal lives and we want to share those blessings with everyone who desires them. We provide instruments, accessories, repairs, sheet music, and training opportunities.</p>\r\n    <p>We sell new and used instruments. We also sell a variety of accessories for these instruments. These accessories include reeds, harp strings, instrument cases, bows, and rosin. In addition, have a very popular “rent-to-own” option and have worked closely with local school districts to be the preferred school instrument rental company. We rent both new and used instruments.</p>\r\n\r\n    <h3>Services</h3>\r\n    <p>We also provide several other services to the music community. We have a team of piano experts on staff that can be hired out to tune or move a piano. In addition, we have a repair shop in the building that allows a wide variety of instruments to be repaired or reconditioned. If the repair is beyond the capabilities at our store, we have preferred partners we recommend the instrument owners use. Our company doesn’t offer lessons, per se. However, we facilitate the connection of students with potential teachers. We keep track of teachers, with information volunteered by the teachers. Contact information, credentials, and availability are some of the details included.</p>\r\n    <p>We have several rooms available for rent. We have a large recital hall in the basement with two grand pianos. The sound quality of the room is excellent so there has historically been a high demand especially on Saturdays or Friday nights. The hall is charged on an hourly rate. We also have several smaller lesson or practice rooms that can be reserved on an ongoing basis. Many teachers find this a very practical location to offer lessons. For example, we have a teacher that reserves a piano room from 4-7 PM on Thursdays to teach lessons. The rooms are soundproofed, so guitar lessons can be held in the adjacent room at the same time as the piano lessons.</p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/users/scott laptop/documents/mariah/intex/intex-ii/homepage/templates/about.html", "uri": "about.html", "source_encoding": "utf-8", "line_map": {"29": 0, "36": 1, "41": 12, "47": 4, "53": 4, "59": 53}}
__M_END_METADATA
"""

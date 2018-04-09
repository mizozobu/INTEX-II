# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520126510.828179
_enable_loop = True
_template_filename = 'C:/Users/hamcm/Desktop/S0/fomo/homepage/templates/contact.html'
_template_uri = 'contact.html'
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
        csrf_input = context.get('csrf_input', UNDEFINED)
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
        csrf_input = context.get('csrf_input', UNDEFINED)
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <h3>Contact us</h3>\r\n        <br />\r\n        <div class="form-container">\r\n            <form action="/contact/" method="POST">\r\n              ')
        __M_writer(str( csrf_input ))
        __M_writer('\r\n              <div class="form-group">\r\n                <label for="inputEmail1">Email address</label>\r\n                <input type="email" class="form-control" id="inputEmail1" name="email" aria-describedby="emailHelp" placeholder="Email">\r\n                <small id="emailHelp" class="form-text text-muted">We\'ll never share your email with anyone else.</small>\r\n              </div>\r\n              <div class="form-group">\r\n                <label for="inputPassword1">Subject</label>\r\n                <input type="text" class="form-control" id="Subject" name="subject"placeholder="Subject">\r\n              </div>\r\n              <div class="form-group">\r\n                <label for="inputPassword1">Comment</label>\r\n                <textarea type="text" class="form-control" id="Comment" name="comment" placeholder="Comment" rows="8"></textarea>\r\n              </div>\r\n              <br />\r\n              <button class="btn-react" type="submit" class="btn btn-success">Submit</button>\r\n            </form>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/hamcm/Desktop/S0/fomo/homepage/templates/contact.html", "uri": "contact.html", "source_encoding": "utf-8", "line_map": {"29": 0, "37": 1, "42": 28, "48": 3, "55": 3, "56": 9, "57": 9, "63": 57}}
__M_END_METADATA
"""

from django.shortcuts import render_to_response
from django.template import RequestContext, Context, Template
from django.template.loader import get_template
from django.core.urlresolvers import reverse
from django.http import HttpResponse
import inspect
from utils.json import json_encode

def rtr(template):
    data = inspect.currentframe().f_back.f_locals
    request = data['request']
    return render_to_response(template,
                              data,
                              context_instance=RequestContext(request))


def rurl(name, *args):
    return reverse(name, args=args)

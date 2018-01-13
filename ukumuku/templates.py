import os
import settings

from .cache import get_from_cache, set_value_in_cache

from mako.template import Template
from mako.lookup import TemplateLookup


templates_directories = []
for directory in os.listdir(settings.BASE_LOOKUP_DIR):
    sub_directory = os.path.join(settings.BASE_LOOKUP_DIR, directory, 'templates')
    if directory == 'templates':
        templates_directories.append(directory)
    elif os.path.isdir(sub_directory):
        templates_directories.append(sub_directory)
template_lookup = TemplateLookup(directories=templates_directories)


def render_template(template_name, context={}):
    
    mytemplate = template_lookup.get_template(template_name)
    return mytemplate.render(**context)

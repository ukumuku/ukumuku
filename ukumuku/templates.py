import os
import settings

from .cache import get_from_cache, set_value_in_cache

from mako.template import Template
from mako.lookup import TemplateLookup


class TemplateEngine():

    def __init__(self):
        templates_directories = []
        for directory in os.listdir(settings.BASE_LOOKUP_DIR):
            sub_directory = os.path.join(settings.BASE_LOOKUP_DIR, directory, 'templates')
            if directory == 'templates':
                templates_directories.append(
                    os.path.join(settings.BASE_LOOKUP_DIR, directory)
                )
            elif os.path.isdir(sub_directory):
                templates_directories.append(sub_directory)
        self.template_lookup = TemplateLookup(directories=templates_directories)
        self.render_template = self._render_template

    def _render_template(self, template_name, context={}):
        return self.template_lookup.get_template(template_name).render(**context)


template_engine = TemplateEngine()
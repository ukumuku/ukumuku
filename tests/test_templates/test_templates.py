import unittest
import mock

from tests.utils import load_settings


class TestTemplates(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_simple_render_template(self):
        load_settings('test_templates/settings.py')
        import ukumuku.templates

        result = ukumuku.templates.render_template('index.html', {'name' : 'Andrix'})
        self.assertEqual(result, 'Hello, Andrix!')
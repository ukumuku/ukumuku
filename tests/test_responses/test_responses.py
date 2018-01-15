import unittest
import mock

from tests.utils import load_settings


class TestResponses(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_simple_http_response(self):
        load_settings('test_responses/settings.py')
        from ukumuku.responses import HttpResponse
        http_response = HttpResponse('hello!')
        self.assertEqual(http_response.body, 'hello!')

    def test_json_response(self):
        load_settings('test_responses/settings.py')
        from ukumuku.responses import JSONResponse
        json_response = JSONResponse({'count' : 1})
        self.assertEqual(json_response.body, '{"count": 1}')

    def test_template_response(self):
        load_settings('test_responses/settings.py')
        from ukumuku.responses import TemplateResponse
        template_response = TemplateResponse('index.html', {'name' : 'Andrix'})
        self.assertEqual(template_response.body, 'Hello, Andrix!')
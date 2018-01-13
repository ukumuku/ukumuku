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

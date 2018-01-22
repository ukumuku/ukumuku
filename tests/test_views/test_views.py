import unittest
import mock

from tests.utils import load_settings
from falcon.request import Request
from falcon.response import Response

class TestTemplates(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_views(self):
        load_settings('test_templates/settings.py')
        from ukumuku.views import View

        req = mock.Mock()
        resp = Response()
        view = View()

        view.get = mock.Mock()
        view.on_get(req, resp)
        view.get.assert_called_with(req)

        view.post = mock.Mock()
        view.on_post(req, resp)
        view.post.assert_called_with(req)

        view.put = mock.Mock()
        view.on_put(req, resp)
        view.put.assert_called_with(req)

        view.patch = mock.Mock()
        view.on_patch(req, resp)
        view.patch.assert_called_with(req)

        view.head = mock.Mock()
        view.on_head(req, resp)
        view.head.assert_called_with(req)

        view.delete = mock.Mock()
        view.on_delete(req, resp)
        view.delete.assert_called_with(req)

    def test_views_not_implemented(self):
        load_settings('test_templates/settings.py')
        from ukumuku.views import View
        import ukumuku

        req = mock.Mock()
        resp = Response()
        view = View()

        view.on_get(req, resp)
        self.assertEqual(resp.status, ukumuku.HTTP_501)

        resp = Response()
        view.on_post(req, resp)
        self.assertEqual(resp.status, ukumuku.HTTP_501)

        resp = Response()
        view.on_put(req, resp)
        self.assertEqual(resp.status, ukumuku.HTTP_501)

        resp = Response()
        view.on_patch(req, resp)
        self.assertEqual(resp.status, ukumuku.HTTP_501)

        resp = Response()
        view.on_head(req, resp)
        self.assertEqual(resp.status, ukumuku.HTTP_501)

        resp = Response()
        view.on_delete(req, resp)
        self.assertEqual(resp.status, ukumuku.HTTP_501)
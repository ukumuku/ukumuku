import json

from falcon.response import Response, ResponseOptions
from .status_codes import *
from .templates import render_template


class HttpResponse(Response):

    def __init__(
        self, body, 
        status=HTTP_200, 
        headers={}, content_type=None, options=None
    ):
        self.status = status
        self._headers = {}

        self._options = options

        self._cookies = None
        self._media = None

        self.body = body
        self.data = None
        self.stream = None
        self.stream_len = None

        self.context = self.context_type()
        # self.body = body
        # self.status = status
        self.content_type = content_type
        self._headers['content-type'] = content_type
        self.to_response = self._to_response

    @property
    def options(self):
        if not self._options:
            self._options = ResponseOptions()
        return self._options

    def _to_response(self, resp):
        pass
        resp.status = self.status
        resp.content_type = self.content_type
        
        if self._options:
            resp.options = self._options

        resp.body = self.body
        resp.data = self.data
        resp.stream = self.stream
        resp.stream_len = self.stream_len
        resp.context = self.context

        resp._cookies = self._cookies
        resp._media = self._media
        resp._headers = self._headers
        

class JSONResponse(HttpResponse):
    def __init__(
        self, context,
        status=HTTP_200, headers={}, 
        content_type='application/json', options=None
    ):
        super(JSONResponse, self).__init__(
            json.dumps(context),
            status, headers, content_type, options
        )


class TemplateResponse(HttpResponse):
    def __init__(
        self, template_name, context,
        status=HTTP_200, headers={}, 
        content_type='text/html', options=None
    ):
        super(TemplateResponse, self).__init__(
            render_template(template_name, context),
            status, headers, content_type, options
        )
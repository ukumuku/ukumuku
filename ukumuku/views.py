import ukumuku.status_codes as status_codes
from ukumuku.responses import HttpResponse

class View:

    def get(self, req, **kwargs):
        return HttpResponse(status=status_codes.HTTP_501)

    def post(self, req, **kwargs):
        return HttpResponse(status=status_codes.HTTP_501)

    def put(self, req, **kwargs):
        return HttpResponse(status=status_codes.HTTP_501)

    def patch(self, req, **kwargs):
        return HttpResponse(status=status_codes.HTTP_501)

    def delete(self, req, **kwargs):
        return HttpResponse(status=status_codes.HTTP_501)

    def head(self, req, **kwargs):
        return HttpResponse(status=status_codes.HTTP_501)

    def on_get(self, req, resp, **kwargs):
        self.get(req, **kwargs).to_response(resp)

    def on_post(self, req, resp, **kwargs):
        self.post(req, **kwargs).to_response(resp)

    def on_put(self, req, resp, **kwargs):
        self.put(req, **kwargs).to_response(resp)

    def on_patch(self, req, resp, **kwargs):
        self.patch(req, **kwargs).to_response(resp)

    def on_delete(self, req, resp, **kwargs):
        self.delete(req, **kwargs).to_response(resp)

    def on_head(self, req, resp, **kwargs):
        self.head(req, **kwargs).to_response(resp)
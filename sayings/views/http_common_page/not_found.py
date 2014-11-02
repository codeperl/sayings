from pyramid.view import notfound_view_config
from pyramid.httpexceptions import HTTPNotFound


class NotFound(HTTPNotFound):
    def __init__(self, request):
        self.request = request

    @notfound_view_config(route_name='http_common_page_not_found',
                          renderer="sayings:templates/http_common_page/not_found/not_found_404.jinja2")
    def not_found(self):
        self.request.response.status = 404
        return {}
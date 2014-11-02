from pyramid.view import view_config
from pyramid.renderers import get_renderer


class Blog(object):
    def __init__(self, request):
        self.request = request

    @view_config(route_name="blog", renderer='sayings:templates/blog/blog/index.jinja2')
    def index(self):
        return {'project': 'Blog'}
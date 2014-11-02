from pyramid.renderers import get_renderer
from pyramid.view import view_config


class Forum(object):
    def __init__(self, request):
        self.request = request

    @view_config(route_name="forum", renderer="sayings:templates/forum/forum/index.jinja2")
    def index(self):
        return {'project': 'Forum index'}

    @view_config(route_name="forum_about", renderer="sayings:templates/forum/forum/about.jinja2")
    def about(self):
        return {'project': 'Forum about'}

from pyramid.view import view_config
from pyramid.renderers import get_renderer


class User(object):
    def __init__(self, request):
        self.request = request

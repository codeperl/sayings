from pyramid.view import view_config


class Home(object):
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home', renderer='sayings:templates/home/home/index.jinja2')
    def index(self):
        return {'project': 'sayings'}
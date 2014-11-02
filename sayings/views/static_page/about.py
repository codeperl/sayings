from pyramid.view import view_config


class About(object):
    def __init__(self, request):
        self.request = request

    @view_config(route_name='static_page_about', renderer='sayings:templates/static_page/about/about.jinja2')
    def about(self):
        return {'project': 'sayings'}
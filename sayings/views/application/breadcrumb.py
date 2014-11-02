from pyramid.view import view_config


class Breadcrumb(object):
    def __init__(self, request):
        self.request = request

    @view_config(route_name="application_breadcrumb",
                 renderer="sayings:templates/application/breadcrumb/breadcrumb.jinja2")
    def breadcrumb(self):
        return {}
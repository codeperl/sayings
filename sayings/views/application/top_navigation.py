from pyramid.view import view_config


class TopNavigation(object):
    def __init__(self, request):
        self.request = request

    @view_config(route_name="application_top_navigation",
                 renderer='sayings:templates/application/top_navigation/top_navigation.jinja2')
    def top_navigation(self):
        return {'authenticated': True}
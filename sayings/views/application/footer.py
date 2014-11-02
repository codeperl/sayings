from pyramid.view import view_config


class Footer(object):
    def __init__(self, request):
        self.request = request

    @view_config(route_name="application_footer", renderer='sayings:templates/application/footer/footer.jinja2')
    def footer(self):
        return {}
from pyramid.view import view_config


class HomeBlock(object):
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home_block_leading_container',
                 renderer='sayings:templates/home/home_block/leading_container.jinja2')
    def leading_container(self):
        return {}

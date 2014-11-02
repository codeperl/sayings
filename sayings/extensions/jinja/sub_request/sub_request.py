from jinja2 import nodes
from jinja2.ext import Extension
from pyramid.request import Request
from webhelpers.html import literal


class SubRequestExtension(Extension):
    """jinja2 subrequest extension to create sub request from *.jinja2 files.
    It depends on pyramid request object and webhelpers module.
    """

    tags = set(['sub_request'])

    def __init__(self, environment):
        super(SubRequestExtension, self).__init__(environment)

    def parse(self, parser):
        line_no = parser.stream.next().lineno
        args = [parser.parse_expression()]

        return nodes.Output([self.call_method('sub_request', args),]).set_lineno(line_no)

    @staticmethod
    def sub_request(dictionary):
        request = dictionary['request']
        route = dictionary['route']
        url = request.route_url(route)
        sub_request = Request.blank(url)
        response = request.invoke_subrequest(sub_request)
        body = literal('%s' %response.body)

        return body
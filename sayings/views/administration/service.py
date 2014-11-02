from pyramid.view import view_config
from sayings.models.services.service_service import ServiceService
from sayings.models.services.builders.forms.service_form_builder import ServiceFormBuilder
from pyramid.httpexceptions import HTTPFound
from sayings.models.entities.service import Service as ServiceModel
from sayings.configs.application_configurations import request_method


class Service(object):
    def __init__(self, request):
        self.request = request
        self.service_service = ServiceService(request)
        self.service_form_builder = ServiceFormBuilder(request)

    @view_config(route_name='administration_service', renderer='sayings:templates/administration/service/index.jinja2')
    def index(self):
        services = self.service_service.find_all()
        return {'services': services}

    @view_config(route_name='administration_service_add',
                 renderer='sayings:templates/administration/service/add.jinja2')
    def add(self):
        service = ServiceModel()
        form = self.service_form_builder.build_create_form().get_form()

        if self.request.method == request_method.POST:
            if form.validate():
                form.populate_obj(service)
                self.service_form_builder.insert(service)
                return HTTPFound(location=self.request.route_url('administration_service'))
        return {'form': form}

    @view_config(route_name='administration_service_edit',
                 renderer='sayings:templates/administration/service/edit.jinja2')
    def edit(self):
        id = int(self.request.matchdict['slug'])
        service = self.service_service.find_one_by_id(id)

        if not service:
            return HTTPFound(location=self.request.route_url('http_common_page_not_found'))

        form = self.service_form_builder.build_update_form(service).get_form()

        if self.request.method == request_method.POST:
            if form.validate():
                form.populate_obj(service)
                self.service_service.update(service)
                return HTTPFound(location=self.request.route_url('administration_service'))
        return {'form': form}

    @view_config(route_name='administration_service_view',
                 renderer='sayings:templates/administration/service/view.jinja2')
    def view(self):
        id = int(self.request.matchdict['slug'])
        service = self.service_service.find_one_by_id(id)

        if not service:
            return HTTPFound(location=self.request.route_url('http_common_page_not_found'))
        return {'service': service}

    @view_config(route_name='administration_service_remove',
                 renderer='sayings:templates/administration/service/remove.jinja2')
    def remove(self):
        id = int(self.request.matchdict['slug'])

        service = self.service_service.find_one_by_id(id)

        if not service:
            return HTTPFound(location=self.request.route_url('http_common_page_not_found'))

        self.service_service.remove(service)
        return HTTPFound(location=self.request.route_url('administration_service'))
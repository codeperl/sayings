from pyramid.view import view_config
from sayings.models.services.role_service import RoleService
from sayings.models.services.builders.forms.role_form_builder import RoleFormBuilder
from pyramid.httpexceptions import HTTPFound
from sayings.models.entities.role import Role as RoleModel
from sayings.configs.application_configurations import request_method


class Role(object):
    def __init__(self, request):
        self.request = request
        self.role_service = RoleService(request)
        self.role_form_builder = RoleFormBuilder(request)

    @view_config(route_name='administration_role', renderer='sayings:templates/administration/role/index.jinja2')
    def index(self):
        roles = self.role_service.find_all()
        return {'roles': roles}

    @view_config(route_name='administration_role_add', renderer='sayings:templates/administration/role/add.jinja2')
    def add(self):
        role = RoleModel()
        form = self.role_form_builder.build_create_form().get_form()

        if self.request.method == request_method.POST:
            if form.validate():
                form.populate_obj(role)
                self.role_service.insert(role)
                return HTTPFound(location=self.request.route_url('administration_role'))
        return {'form': form}

    @view_config(route_name='administration_role_edit', renderer='sayings:templates/administration/role/edit.jinja2')
    def edit(self):
        id = int(self.request.matchdict['slug'])
        role = self.role_service.find_one_by_id(id)

        if not role:
            return HTTPFound(location=self.request.route_url('http_common_page_not_found'))

        form = self.role_form_builder.build_update_form(role).get_form()

        if self.request.method == request_method.POST:
            if form.validate():
                form.populate_obj(role)
                self.role_service.update(role)
                return HTTPFound(location=self.request.route_url('administration_role'))
        return {'form': form}

    @view_config(route_name='administration_role_view', renderer='sayings:templates/administration/role/view.jinja2')
    def view(self):
        id = int(self.request.matchdict['slug'])
        role = self.role_service.find_one_by_id(id)

        if not role:
            return HTTPFound(location=self.request.route_url('http_common_page_not_found'))
        return {'role': role}

    @view_config(route_name='administration_role_remove',
                 renderer='sayings:templates/administration/role/remove.jinja2')
    def remove(self):
        id = int(self.request.matchdict['slug'])

        role = self.role_service.find_one_by_id(id)

        if not role:
            return HTTPFound(location=self.request.route_url('http_common_page_not_found'))

        self.role_service.remove(role)
        return HTTPFound(location=self.request.route_url('administration_role'))
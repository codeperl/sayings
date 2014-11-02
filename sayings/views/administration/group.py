from pyramid.view import view_config
from sayings.models.services.builders.forms.group_form_builder import GroupFormBuilder
from sayings.models.services.group_service import GroupService
from pyramid.httpexceptions import HTTPFound
from sayings.models.entities.group import Group as GroupModel
from sayings.configs.application_configurations import request_method


class Group(object):
    def __init__(self, request):
        self.request = request
        self.group_service = GroupService(request)
        self.group_form_builder = GroupFormBuilder(request)

    @view_config(route_name='administration_group', renderer='sayings:templates/administration/group/index.jinja2')
    def index(self):
        groups = self.group_service.find_all()
        return {'groups': groups}

    @view_config(route_name='administration_group_add', renderer='sayings:templates/administration/group/add.jinja2')
    def add(self):
        group = GroupModel()
        form = self.group_form_builder.build_create_form().get_form()

        if self.request.method == request_method.POST:
            if form.validate():
                form.populate_obj(group)
                self.group_service.insert(group)
                return HTTPFound(location=self.request.route_url('administration_group'))
        return {'form': form}

    @view_config(route_name='administration_group_edit', renderer='sayings:templates/administration/group/edit.jinja2')
    def edit(self):
        id = int(self.request.matchdict['slug'])
        group = self.group_service.find_one_by_id(id)

        if not group:
            return HTTPFound(location=self.request.route_url('http_common_page_not_found'))

        form = self.group_form_builder.build_update_form(group).get_form()

        if self.request.method == request_method.POST:
            if form.validate():
                form.populate_obj(group)
                self.group_service.update(group)
                return HTTPFound(location=self.request.route_url('administration_group'))
        return {'form': form}

    @view_config(route_name='administration_group_view', renderer='sayings:templates/administration/group/view.jinja2')
    def view(self):
        id = int(self.request.matchdict['slug'])
        group = self.group_service.find_one_by_id(id)

        if not group:
            return HTTPFound(location=self.request.route_url('http_common_page_not_found'))
        return {'group': group}

    @view_config(route_name='administration_group_remove',
                 renderer='sayings:templates/administration/group/remove.jinja2')
    def remove(self):
        id = int(self.request.matchdict['slug'])

        group = self.group_service.find_one_by_id(id)

        if not group:
            return HTTPFound(location=self.request.route_url('http_common_page_not_found'))

        self.group_service.remove(group)
        return HTTPFound(location=self.request.route_url('administration_group'))
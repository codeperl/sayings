from pyramid.view import view_config
from sayings.models.services.user_service import UserService
from sayings.models.services.builders.forms.user_form_builder import UserFormBuilder
from pyramid.httpexceptions import HTTPFound
from sayings.models.entities.user import User as UserModel
from sayings.configs.application_configurations import request_method


class User(object):
    def __init__(self, request):
        self.request = request
        self.user_service = UserService(request)
        self.user_form_builder = UserFormBuilder(request)

    @view_config(route_name='administration_user', renderer='sayings:templates/administration/user/index.jinja2')
    def index(self):
        users = self.user_service.find_all()
        return {'users': users}

    @view_config(route_name='administration_user_add', renderer='sayings:templates/administration/user/add.jinja2')
    def add(self):
        user = UserModel()
        form = self.user_form_builder.build_create_form().get_form()

        if self.request.method == request_method.POST:
            if form.validate():
                form.populate_obj(user)
                self.user_service.insert(user)
                return HTTPFound(location=self.request.route_url('administration_user'))
        return {'form': form}

    @view_config(route_name='administration_user_edit', renderer='sayings:templates/administration/user/edit.jinja2')
    def edit(self):
        id = int(self.request.matchdict['slug'])
        user = self.user_service.find_one_by_id(id)

        if not user:
            return HTTPFound(location=self.request.route_url('http_common_page_not_found'))

        form = self.user_form_builder.build_update_form(user).get_form()

        if self.request.method == request_method.POST:
            if form.validate():
                form.populate_obj(user)
                self.user_service.update(user)
                return HTTPFound(location=self.request.route_url('administration_user'))
        return {'form': form}

    @view_config(route_name='administration_user_view', renderer='sayings:templates/administration/user/view.jinja2')
    def view(self):
        id = int(self.request.matchdict['slug'])
        user = self.user_service.find_one_by_id(id)

        if not user:
            return HTTPFound(location=self.request.route_url('http_common_page_not_found'))
        return {'user': user}

    @view_config(route_name='administration_user_remove',
                 renderer='sayings:templates/administration/user/remove.jinja2')
    def remove(self):
        id = int(self.request.matchdict['slug'])

        user = self.user_service.find_one_by_id(id)

        if not user:
            return HTTPFound(location=self.request.route_url('http_common_page_not_found'))

        self.user_service.remove(user)
        return HTTPFound(location=self.request.route_url('administration_user'))
from pyramid.view import view_config
from sayings.models.services.page_service import PageService
from sayings.models.services.builders.forms.page_form_builder import PageFormBuilder
from sayings.models.entities.page import Page as PageModel
from pyramid.httpexceptions import HTTPFound
from sayings.configs.application_configurations import request_method


class Page(object):
    def __init__(self, request):
        self.request = request
        self.page_service = PageService(request)
        self.page_form_builder = PageFormBuilder(request)

    @view_config(route_name='administration_page', renderer='sayings:templates/administration/page/index.jinja2')
    def index(self):
        pages = self.page_service.find_all()
        return {'pages': pages}

    @view_config(route_name='administration_page_add', renderer='sayings:templates/administration/page/add.jinja2')
    def add(self):
        page = PageModel()
        form = self.page_form_builder.build_create_form().get_form()

        if self.request.method == request_method.POST:
            if form.validate():
                form.populate_obj(page)
                self.page_service.insert(page)
                return HTTPFound(location=self.request.route_url('administration_page'))
        return {'form': form}

    @view_config(route_name='administration_page_edit', renderer='sayings:templates/administration/page/edit.jinja2')
    def edit(self):
        id = int(self.request.matchdict['slug'])
        page = self.page_service.find_one_by_id(id)

        if not page:
            return HTTPFound(location=self.request.route_url('http_common_page_not_found'))

        form = self.page_form_builder.build_update_form(page).get_form()

        if self.request.method == request_method.POST:
            if form.validate():
                form.populate_obj(page)
                self.page_service.update(page)
                return HTTPFound(location=self.request.route_url('administration_page'))
        return {'form': form}

    @view_config(route_name='administration_page_view', renderer='sayings:templates/administration/page/view.jinja2')
    def view(self):
        id = int(self.request.matchdict['slug'])
        page = self.page_service.find_one_by_id(id)

        if not page:
            return HTTPFound(location=self.request.route_url('http_common_page_not_found'))
        return {'page': page}

    @view_config(route_name='administration_page_remove',
                 renderer='sayings:templates/administration/page/remove.jinja2')
    def remove(self):
        id = int(self.request.matchdict['slug'])

        page = self.page_service.find_one_by_id(id)

        if not page:
            return HTTPFound(location=self.request.route_url('http_common_page_not_found'))

        self.page_service.remove(page)
        return HTTPFound(location=self.request.route_url('administration_page'))
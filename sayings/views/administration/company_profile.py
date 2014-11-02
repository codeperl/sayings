from pyramid.view import view_config
from sayings.models.services.builders.forms.company_profile_form_builder import CompanyProfileFormBuilder
from sayings.models.services.company_profile_service import CompanyProfileService
from pyramid.httpexceptions import HTTPFound
from sayings.models.entities.company_profile import CompanyProfile as CompanyProfileModel
from sayings.configs.application_configurations import request_method


class CompanyProfile(object):
    def __init__(self, request):
        self.request = request
        self.company_profile_service = CompanyProfileService(request)
        self.company_profile_form_builder = CompanyProfileFormBuilder(request)

    @view_config(route_name='administration_company_profile',
                 renderer='sayings:templates/administration/company_profile/index.jinja2')
    def index(self):
        company_profiles = self.company_profile_service.find_all()
        return {'company_profiles': company_profiles}

    @view_config(route_name='administration_company_profile_add',
                 renderer='sayings:templates/administration/company_profile/add.jinja2')
    def add(self):
        company_profile = CompanyProfileModel()
        form = self.company_profile_form_builder.build_create_form().get_form()

        if self.request.method == request_method.POST:
            if form.validate():
                form.populate_obj(company_profile)
                self.company_profile_service.insert(company_profile)
                return HTTPFound(location=self.request.route_url('administration_company_profile'))
        return {'form': form}

    @view_config(route_name='administration_company_profile_edit',
                 renderer='sayings:templates/administration/company_profile/edit.jinja2')
    def edit(self):
        id = int(self.request.matchdict['slug'])
        company_profile = self.company_profile_service.find_one_by_id(id)

        if not company_profile:
            return HTTPFound(location=self.request.route_url('http_common_page_not_found'))

        form = self.company_profile_form_builder.build_update_form(company_profile).get_form()

        if self.request.method == request_method.POST:
            if form.validate():
                form.populate_obj(company_profile)
                self.company_profile_service.update(company_profile)
                return HTTPFound(location=self.request.route_url('administration_company_profile'))
        return {'form': form}

    @view_config(route_name='administration_company_profile_view',
                 renderer='sayings:templates/administration/company_profile/view.jinja2')
    def view(self):
        id = int(self.request.matchdict['slug'])
        company_profile = self.company_profile_service.find_one_by_id(id)

        if not company_profile:
            return HTTPFound(location=self.request.route_url('http_common_page_not_found'))
        return {'company_profile': company_profile}

    @view_config(route_name='administration_company_profile_remove',
                 renderer='sayings:templates/administration/company_profile/remove.jinja2')
    def remove(self):
        id = int(self.request.matchdict['slug'])

        company_profile = self.company_profile_service.find_one_by_id(id)

        if not company_profile:
            return HTTPFound(location=self.request.route_url('http_common_page_not_found'))

        self.company_profile_service.remove(company_profile)
        return HTTPFound(location=self.request.route_url('administration_company_profile'))
from pyramid.view import view_config
from sayings.models.services.builders.forms.individual_profile_form_builder import IndividualProfileFormBuilder
from sayings.models.services.individual_profile_service import IndividualProfileService
from pyramid.httpexceptions import HTTPFound
from sayings.models.entities.individual_profile import IndividualProfile as IndividualProfileModel
from sayings.configs.application_configurations import request_method


class IndividualProfile(object):
    def __init__(self, request):
        self.request = request
        self.individual_profile_service = IndividualProfileService(request)
        self.individual_profile_form_builder = IndividualProfileFormBuilder(request)

    @view_config(route_name='administration_individual_profile',
                 renderer='sayings:templates/administration/individual_profile/index.jinja2')
    def index(self):
        individual_profiles = self.individual_profile_service.find_all()
        return {'individual_profiles': individual_profiles}

    @view_config(route_name='administration_individual_profile_add',
                 renderer='sayings:templates/administration/individual_profile/add.jinja2')
    def add(self):
        individual_profile = IndividualProfileModel()
        form = self.individual_profile_form_builder.build_create_form().get_form()

        if self.request.method == request_method.POST:
            if form.validate():
                form.populate_obj(individual_profile)
                self.individual_profile_service.insert(individual_profile)
                return HTTPFound(location=self.request.route_url('administration_individual_profile'))
        return {'form': form}

    @view_config(route_name='administration_individual_profile_edit',
                 renderer='sayings:templates/administration/individual_profile/edit.jinja2')
    def edit(self):
        id = int(self.request.matchdict['slug'])
        individual_profile = self.individual_profile_service.find_one_by_id(id)

        if not individual_profile:
            return HTTPFound(location=self.request.route_url('http_common_page_not_found'))

        form = self.individual_profile_form_builder.build_update_form(individual_profile).get_form()

        if self.request.method == request_method.POST:
            if form.validate():
                form.populate_obj(individual_profile)
                self.individual_profile_service.update(individual_profile)
                return HTTPFound(location=self.request.route_url('administration_individual_profile'))
        return {'form': form}

    @view_config(route_name='administration_individual_profile_view',
                 renderer='sayings:templates/administration/individual_profile/view.jinja2')
    def view(self):
        id = int(self.request.matchdict['slug'])
        individual_profile = self.individual_profile_service.find_one_by_id(id)

        if not individual_profile:
            return HTTPFound(location=self.request.route_url('http_common_page_not_found'))
        return {'individual_profile': individual_profile}

    @view_config(route_name='administration_individual_profile_remove',
                 renderer='sayings:templates/administration/individual_profile/remove.jinja2')
    def remove(self):
        id = int(self.request.matchdict['slug'])

        individual_profile = self.individual_profile_service.find_one_by_id(id)

        if not individual_profile:
            return HTTPFound(location=self.request.route_url('http_common_page_not_found'))

        self.individual_profile_service.remove(individual_profile)
        return HTTPFound(location=self.request.route_url('administration_individual_profile'))
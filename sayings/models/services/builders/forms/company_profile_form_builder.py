from sayings.forms.company_profile_add_form import CompanyProfileAddForm
from sayings.forms.company_profile_edit_form import CompanyProfileEditForm


class CompanyProfileFormBuilder(object):
    """ Company profile form builder
    """

    def __init__(self, request):
        self.request = request
        self.form = None

    def build_create_form(self):
        self.form = CompanyProfileAddForm(self.request.POST, meta={'csrf_context': self.request.client_addr})
        return self

    def build_update_form(self, group):
        self.form = CompanyProfileEditForm(self.request.POST, group, meta={'csrf_context': self.request.client_addr})
        return self

    def get_form(self):
        return self.form
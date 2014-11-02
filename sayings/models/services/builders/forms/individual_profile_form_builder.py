from sayings.forms.individual_profile_add_form import IndividualProfileAddForm
from sayings.forms.individual_profile_edit_form import IndividualProfileEditForm


class IndividualProfileFormBuilder(object):
    """ Individual profile form builder
    """

    def __init__(self, request):
        self.request = request
        self.form = None

    def build_create_form(self):
        self.form = IndividualProfileAddForm(self.request.POST, meta={'csrf_context': self.request.client_addr})
        return self

    def build_update_form(self, group):
        self.form = IndividualProfileEditForm(self.request.POST, group, meta={'csrf_context': self.request.client_addr})
        return self

    def get_form(self):
        return self.form
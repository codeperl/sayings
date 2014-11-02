from sayings.forms.service_add_form import ServiceAddForm
from sayings.forms.service_edit_form import ServiceEditForm


class ServiceFormBuilder(object):
    """ service form builder
    """

    def __init__(self, request):
        self.request = request
        self.form = None

    def build_create_form(self):
        self.form = ServiceAddForm(self.request.POST, meta={'csrf_context': self.request.client_addr})
        return self

    def build_update_form(self, group):
        self.form = ServiceEditForm(self.request.POST, group, meta={'csrf_context': self.request.client_addr})
        return self

    def get_form(self):
        return self.form
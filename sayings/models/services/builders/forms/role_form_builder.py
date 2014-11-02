from sayings.forms.role_add_form import RoleAddForm
from sayings.forms.role_edit_form import RoleEditForm


class RoleFormBuilder(object):
    """ role form builder
    """

    def __init__(self, request):
        self.request = request
        self.form = None

    def build_create_form(self):
        self.form = RoleAddForm(self.request.POST, meta={'csrf_context': self.request.client_addr})
        return self

    def build_update_form(self, group):
        self.form = RoleEditForm(self.request.POST, group, meta={'csrf_context': self.request.client_addr})
        return self

    def get_form(self):
        return self.form
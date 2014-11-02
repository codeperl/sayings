from sayings.forms.user_add_form import UserAddForm
from sayings.forms.user_edit_form import UserEditForm


class UserFormBuilder(object):
    """ user form builder
    """

    def __init__(self, request):
        self.request = request
        self.form = None

    def build_create_form(self):
        self.form = UserAddForm(self.request.POST, meta={'csrf_context': self.request.client_addr})
        return self

    def build_update_form(self, group):
        self.form = UserEditForm(self.request.POST, group, meta={'csrf_context': self.request.client_addr})
        return self

    def get_form(self):
        return self.form
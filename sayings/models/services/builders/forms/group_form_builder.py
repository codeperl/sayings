from sayings.forms.group_add_form import GroupAddForm
from sayings.forms.group_edit_form import GroupEditForm


class GroupFormBuilder(object):
    """ group form builder
    """

    def __init__(self, request):
        self.request = request
        self.form = None

    def build_create_form(self):
        self.form = GroupAddForm(self.request.POST, meta={'csrf_context': self.request.client_addr})
        return self

    def build_update_form(self, group):
        self.form = GroupEditForm(self.request.POST, group, meta={'csrf_context': self.request.client_addr})
        return self

    def get_form(self):
        return self.form
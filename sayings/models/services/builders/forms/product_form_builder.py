from sayings.forms.product_add_form import ProductAddForm
from sayings.forms.product_edit_form import ProductEditForm


class ProductFormBuilder(object):
    """ product form builder
    """

    def __init__(self, request):
        self.request = request
        self.form = None

    def build_create_form(self):
        self.form = ProductAddForm(self.request.POST, meta={'csrf_context': self.request.client_addr})
        return self

    def build_update_form(self, group):
        self.form = ProductEditForm(self.request.POST, group, meta={'csrf_context': self.request.client_addr})
        return self

    def get_form(self):
        return self.form
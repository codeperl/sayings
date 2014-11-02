from sayings.forms.contact_form import ContactForm


class ContactFormBuilder(object):
    """ Contact form builder
    """

    def __init__(self, request):
        self.request = request
        self.form = None

    def build(self):
        self.form = ContactForm(self.request.POST, meta={'csrf_context': self.request.client_addr})
        return self

    def get_form(self):
        return self.form
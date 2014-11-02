from pyramid.view import view_config
from sayings.models.services.builders.forms.contact_form_builder import ContactFormBuilder
from sayings.models.entities.contact import Contact as ContactModel
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from sayings.models.services.email_service import EmailService


class Contact(object):
    def __init__(self, request):
        self.request = request
        self.email_service = EmailService(request)
        self.contact_form_builder = ContactFormBuilder(request)

    @view_config(route_name='static_page_contact', renderer='sayings:templates/static_page/contact/contact.jinja2')
    def contact(self):
        contact = ContactModel()
        form = self.contact_form_builder.build().get_form()

        if self.request.method == 'POST':
            if form.validate():
                form.populate_obj(contact)
                self.email_service.send_contact_email("Sample subject", 'code@jam.com', ['it.codeperl@gmal.com'],
                                                      'This is main body')

                return HTTPFound(location=self.request.route_url('static_page_contact'))

        return {'project': 'static_page_contact', 'form': form}
from wtforms.csrf.core import CSRF
from hashlib import md5
from sayings.configs.application_configurations import app_config


class SecureForm(CSRF):

    def setup_form(self, form):
        self.csrf_context = form.meta.csrf_context
        return super(SecureForm, self).setup_form(form)


    def generate_csrf_token(self, csrf_token):
        key = str(app_config.CSRF_PROTECTION_SECRET_KEY) + str(self.csrf_context)
        token = md5(key).hexdigest()
        return token

    def validate_csrf_token(self, form, field):
        if field.data != field.current_token:
            raise ValueError('Invalid CSRF')
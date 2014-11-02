from wtforms_alchemy import ModelForm
from sayings.models.entities.page import Page
import wtforms.validators as FormValidators
from wtforms.fields import SubmitField
from sayings.extensions.wtform.secure_form import SecureForm


class CompanyProfileEditForm(ModelForm):
    """
    Company profile from with wtforms-alchemy integration and implementation.
    """

    class Meta:
        only = ['name', 'content', 'published_at', 'id']
        csrf = True
        csrf_class = SecureForm
        model = Page
        field_args = {
            'name': {
                    'label': 'Name',
                    'validators': [FormValidators.DataRequired()]
                },
            'content': {
                    'label': 'Content',
                    'validators': [FormValidators.DataRequired()]
                },
            'published_at': {
                    'label': 'Published at'
                }
            }

    submit = SubmitField('Edit Company Profile')
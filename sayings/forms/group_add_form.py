from wtforms_alchemy import ModelForm
from sayings.models.entities.group import Group
import wtforms.validators as FormValidators
from wtforms.fields import SubmitField
from sayings.extensions.wtform.secure_form import SecureForm


class GroupAddForm(ModelForm):
    """
    Group from with wtforms-alchemy integration and implementation.
    """

    class Meta:
        only = ['name']
        csrf = True
        csrf_class = SecureForm
        model = Group
        field_args = {
            'name': {
                    'label': 'Name',
                    'validators': [FormValidators.DataRequired()]
                }
            }

    submit = SubmitField('Add Group')
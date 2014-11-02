from wtforms_alchemy import ModelForm
from sayings.models.entities.role import Role
import wtforms.validators as FormValidators
from wtforms.fields import SubmitField
from sayings.extensions.wtform.secure_form import SecureForm


class RoleEditForm(ModelForm):

    class Meta:
        only = ['name', 'active', 'id']
        csrf = True
        csrf_class = SecureForm
        model = Role
        field_args = {
            'name': {
                    'label': 'Name',
                    'validators': [FormValidators.DataRequired()]
                }
            }

    submit = SubmitField('Edit Role')
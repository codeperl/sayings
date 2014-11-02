from wtforms_alchemy import ModelForm
from sayings.models.entities.user import User
import wtforms.validators as FormValidators
from wtforms.fields import SubmitField
from sayings.extensions.wtform.secure_form import SecureForm


class UserEditForm(ModelForm):

    class Meta:
        only = ['email', 'id']
        csrf = True
        csrf_class = SecureForm
        model = User
        field_args = {
            'email': {
                'label': 'Email',
                'validators': [FormValidators.DataRequired(), FormValidators.Email(),
                               FormValidators.Length(min=6, max=120)]
            }
        }

    submit = SubmitField('Edit User')
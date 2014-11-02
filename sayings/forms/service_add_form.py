from wtforms_alchemy import ModelForm
from sayings.models.entities.service import Service
import wtforms.validators as FormValidators
from wtforms.fields import SubmitField
from sayings.extensions.wtform.secure_form import SecureForm
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from sayings.models.repositories.profile_repository import ProfileRepository


class ServiceAddForm(ModelForm):

    class Meta:
        only = ['name', 'content', 'active']
        csrf = True
        csrf_class = SecureForm
        model = Service
        field_args = {
            'name': {
                    'label': 'Name',
                    'validators': [FormValidators.DataRequired()]
                }
            }

    profile = QuerySelectField(query_factory=ProfileRepository().all,
                                allow_blank=False)
    submit = SubmitField('Add Service')
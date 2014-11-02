from sayings.extensions.wtform.secure_form import SecureForm
from wtforms_alchemy import ModelForm


class SecureModelForm(ModelForm, SecureForm):
    def __init__(self):
        ModelForm.__init__()
        SecureForm.__init__()
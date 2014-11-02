from sayings.extensions.wtform.secure_form import SecureForm
from wtforms import StringField, TextAreaField, validators, SubmitField
from wtforms import Form


class ContactForm(Form):
    """Contact form to get the users data and send the email to server.
    """

    class Meta:
        csrf = True
        csrf_class = SecureForm

    email= StringField('Email Address', [validators.email()])
    body= TextAreaField('Message', [validators.Length(min=6, max=350)])
    submit = SubmitField('Send')
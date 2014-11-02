from pyramid_mailer import get_mailer
from pyramid_mailer.message import Message


class EmailService(object):
    """ EmailService is a service to send emails with different purposes.
    """

    def __init__(self, request):
        self.request = request
        self.mailer = get_mailer(request)

        self.subject = None
        self.sender = None
        self.recipients = list()
        self.body = None
        self.message = None

    def create_message(self, subject, sender, recipients, body):
        self.subject = subject
        self.sender = sender
        self.recipients = recipients
        self.body = body

        self.message = Message(
            subject=self.subject,
            sender=self.sender,
            recipients=self.recipients,
            body=self.body
        )

        return self.message

    def send_immediately(self):
        self.mailer.send_immediately(self.message, fail_silently=False)

    def send(self):
        self.mailer.send(self.message)

    def send_contact_email(self, subject, sender, recipients, body):
        self.message = self.create_message(subject, sender, recipients, body)
        self.send_immediately()
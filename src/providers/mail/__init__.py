
from src.objects.factory import ObjectFactory
from .mail_generator import FakeMail, DisposableMail, MailGenerator, CleanFakeMail

class MailFactory(ObjectFactory):

    def retrieve_provider(self, value, email_type) -> MailGenerator:
        if value in ["fake",  "f"]:
            return FakeMail(email_type)
        if value in ["clean", "c"]:
            return CleanFakeMail(email_type)
        if value in ["disposable", "d"]:
            return DisposableMail(email_type)
        return MailGenerator()

def retrieve_mail_provider(name, email_type="gmail.com") -> MailGenerator:
    return MailFactory().retrieve_provider(name, email_type)
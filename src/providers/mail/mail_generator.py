import datetime
import random
import re

from src.objects.agent import Profile
from src.scraper.mail import retrieve_disposable_mail


class MailGenerator(object):

    def __init__(self, email_type) -> None:
        self.email_type = email_type

    def retrieve_email(self, agent: Profile):
        raise NotImplementedError
    
class FakeMail(MailGenerator):
    """
    generates a string in email format
    """
    def __init__(self, email_type) -> None:
        self.email_type = email_type

    @staticmethod
    def __only_alphanumeric(item):
        return re.sub(pattern='^\w+$', string=item, repl="")

    def __generate_email(self, agent: Profile, email_type: str):


        def parse_firstname(f) -> str:
            op = [str(f).lower(), str(f), str(f)[0:3]]
            name = random.choice(op)
            return name
        
        def parse_age(s: datetime.datetime) -> str:
            op = [f"{s.year}", f"{s.year}.{s.month}", f"{str(s.year)[2:]}", f"{s.year}_{s.month}", ""]
            return random.choice(op)

        def parse_lastname(l: Profile) -> str:
            op = [str(self.__only_alphanumeric(l.last_name))[0:1], f"{str(self.__only_alphanumeric(l.last_name)[0:1])}", str(self.__only_alphanumeric(l.last_name)), str(self.__only_alphanumeric(l.last_name)).lower()]
            if l.initial != None:
                op.append(f"{str(l.initial).upper()}.{str(l.last_name)}")
                op.append(f"{str(l.initial).upper()}.{str(l.last_name)[0:1]}")
            return str(random.choice(op)).replace(" ", "")
        
        def get_mail_prefix():
            first_part = parse_firstname(agent.first_name)
            second_part = parse_lastname(agent)
            third_part = parse_age(agent.age)

            return [first_part, second_part, third_part]

        def is_sensible_email(lst):
            """
            at least one of the parts should be longer than 3, 
            to be somewhat sensible.
            """
            return sum(1 for element in lst if len(element) >= 3) >= 2

        email_parts = get_mail_prefix()

        while not is_sensible_email(email_parts):
            email_parts = get_mail_prefix()
            

        prefix = f"{email_parts[0]}{email_parts[1]}{email_parts[2]}"

        return f"{prefix}@{email_type}"
    

    def retrieve_email(self, agent: Profile):
        return self.__generate_email(agent, email_type=self.email_type)
    
class CleanFakeMail(MailGenerator):
    """
    generates a string in email format
    """
    def __init__(self, email_type) -> None:
        self.email_type = email_type

    @staticmethod
    def __only_alphanumeric(item):
        return re.sub(pattern='^\w+$', string=item, repl="")

    def __generate_email(self, agent: Profile, email_type: str):


        def parse_firstname(f) -> str:
            op = [str(f).lower(), str(f)]
            name = random.choice(op)
            return name
        
        def parse_age(s: datetime.datetime) -> str:
            op = [f"{s.year}", f"{str(s.year)[2:]}", ""]
            return random.choice(op)

        def parse_lastname(l: Profile) -> str:
            op = [str(self.__only_alphanumeric(l.last_name)), str(self.__only_alphanumeric(l.last_name)).lower()]
            if l.initial != None:
                op.append(f".{str(l.initial).upper()}.{str(l.last_name)}")
            return str(random.choice(op)).replace(" ", "")
        
        def get_mail_prefix():
            first_part = parse_firstname(agent.first_name)
            second_part = parse_lastname(agent)
            third_part = parse_age(agent.age)

            return [first_part, second_part, third_part]


        def is_sensible_email(lst):
            """
            at least one of the parts should be longer than 3, 
            to be somewhat sensible.
            """
            return sum(1 for element in lst if len(element) >= 3) >= 2

        email_parts = get_mail_prefix()

        while not is_sensible_email(email_parts):
            email_parts = get_mail_prefix()

        prefix = f"{email_parts[0]}{email_parts[1]}{email_parts[2]}"

        return f"{prefix}@{email_type}"
    

    def retrieve_email(self, agent: Profile):
        return self.__generate_email(agent, email_type=self.email_type)
    

class DisposableMail(MailGenerator):
    """
    Retrieves a disposable mail from https://temp-mail.org
    """
    def __init__(self, email_type) -> None:
        self.email_type = email_type

    def __request_email(self):
        return retrieve_disposable_mail()
    
    def retrieve_email(self, agent: Profile):
        return self.__request_email()
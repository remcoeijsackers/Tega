import datetime
import random
from src.agents.objects import AgentStub


class MailHandler(object):

    def retrieve_email(self, agent: AgentStub):
        raise NotImplementedError
    
class FakeMail(MailHandler):
    """
    generates a string in email format
    """

    def __generate_email(self, agent: AgentStub):


        def parse_firstname(f) -> str:
            op = [str(f).lower(), str(f),f"{random.randrange(0, 100)}"]
            name = random.choice(op)
            return name
        
        def parse_age(s: datetime.datetime) -> str:
            op = [f"{s.year}", f"{s.year}.{s.month}", f"{str(s.year)[2:]}", f"{s.year}_{s.month}", ""]
            return random.choice(op)

        def parse_lastname(l: AgentStub) -> str:
            op = [str(l.last_name)[0:1], f"{str(l.last_name)[0:1]}", str(l.last_name), str(l.last_name).lower()]
            if l.initial != None:
                op.append(f"{str(l.initial).upper()}.{str(l.last_name)}")
                op.append(f"{str(l.initial).upper()}.{str(l.last_name)[0:1]}")
            return random.choice(op)
        
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
            return sum(1 for element in lst if len(element) > 3) >= 2

        email_parts = get_mail_prefix()

        while not is_sensible_email(email_parts):
            email_parts = get_mail_prefix()
            

        prefix = f"{email_parts[0]}{email_parts[1]}{email_parts[2]}"

        return f"{prefix}@{self.config.email_type}"
    

    def retrieve_email(self, agent: AgentStub):
        return self.__generate_email(agent)
    

class DisposableMail(MailHandler):
    """
    Retrieves a disposable mail from https://temp-mail.org
    """

    def retrieve_email(self, agent: AgentStub):
        return super().retrieve_email(agent)
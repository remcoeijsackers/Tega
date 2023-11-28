import random
import datetime
from dataclasses import dataclass

from src.scraper.mail_generator import MailHandler

from .objects import Agent, AgentStub
from .constants import last_names, letters, get_first_based_nat,nationality
from ..utils.passwords import generate_password

@dataclass
class MakerConfig(object):
    email_type: str = "gmail.com"
    mail_generator: MailHandler
        

class Maker:
    def __init__(self, settings: MakerConfig) -> None:
        self.config = settings

    def generate(self):
        st = self.__generate_stub()
        st.age = self.__generate_age()
        st.email = self.__generate_email(st)
        st.password = self.__generate_password()
        
        return Agent(**st.__dict__)

    @staticmethod
    def coin_flip():
        return random.choice([True, False])

    @staticmethod
    def __generate_age():
        y = random.randrange(1980, 2001)
        m = random.randrange(1,12)
        d = random.randrange(1,27)
        return datetime.datetime(y,m,d)

    def __generate_stub(self) -> AgentStub:
        l = random.choice(last_names)
        i = str(random.choice(letters)).upper()

        n = random.choice(nationality)

        return AgentStub( **{
             "nat": n,
             "first_name": get_first_based_nat(n),
             "last_name": l,
             "initial": i if self.coin_flip() else None,

        })
    
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
    
    @staticmethod
    def __generate_password() -> str:
        return generate_password(20)

def generate_sample_agent(maker: Maker) -> Agent:
    agent_object = maker.generate()
    return agent_object
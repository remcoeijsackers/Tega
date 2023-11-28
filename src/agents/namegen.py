import random
import datetime
from dataclasses import dataclass

from src.scraper.mail_generator import MailHandler

from .objects import Agent, AgentStub
from .constants import last_names, letters, get_first_based_nat,nationality
from ..utils.passwords import generate_password

@dataclass
class MakerConfig(object):
    mail_generator: MailHandler
    email_type: str = "gmail.com"

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
        return self.config.mail_generator.retrieve_email(
            agent=agent,
            email_type=self.config.email_type
            )
    
    @staticmethod
    def __generate_password() -> str:
        return generate_password(20)

def generate_sample_agent(maker: Maker) -> Agent:
    agent_object = maker.generate()
    return agent_object
import random
import datetime
from dataclasses import dataclass

from src.providers.mail.mail_generator import MailGenerator
from src.providers.profile.profile_generator import ProfileGenerator

from src.objects.agent import Agent, Profile
from src.utils.passwords import generate_password

@dataclass
class MakerConfig(object):
    mail_generator: MailGenerator
    profile_generator: ProfileGenerator

class UserGenerator:
    """
    Generates fake user accounts.
    """
    def __init__(self, settings: MakerConfig) -> None:
        self.config = settings

    def generate(self) -> Agent:
        agent_object = self.generate_profile()

        agent_object.age = self.__generate_age()
        agent_object.email = self.generate_email(agent_object)
        agent_object.password = self.__generate_password()
        
        return Agent(**agent_object.__dict__)

    @staticmethod
    def __generate_password() -> str:
        return generate_password(20)

    @staticmethod
    def __generate_age():
        y = random.randrange(1980, 2001)
        m = random.randrange(1,12)
        d = random.randrange(1,27)
        return datetime.datetime(y,m,d)

    def generate_profile(self) -> Profile:
        return self.config.profile_generator.retrieve_profile()

    def generate_email(self, agent: Profile):
        return self.config.mail_generator.retrieve_email(
            agent=agent
            )
    

def generate_sample_agent(maker: UserGenerator) -> Agent:
    agent_object = maker.generate()
    return agent_object
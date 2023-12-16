import random
import datetime
from dataclasses import dataclass

from src.providers.mail.mail_generator import MailGenerator
from src.providers.password.password_generator import PasswordGenerator
from src.providers.profile.profile_generator import ProfileGenerator
from src.providers.age.age_generator import AgeGenerator

from src.objects.agent import Agent, Profile

@dataclass
class MakerConfig(object):
    mail_generator: MailGenerator
    profile_generator: ProfileGenerator
    password_generator: PasswordGenerator
    age_generator: AgeGenerator

class UserGenerator:
    """
    Generates fake user accounts.
    """
    def __init__(self, settings: MakerConfig) -> None:
        self.config = settings

    def generate(self) -> Agent:
        agent_object = self.generate_profile()
        agent_object.age = self.generate_age()
        agent_object.email = self.generate_email(agent_object)

        agent_object.password = self.generate_password()
        
        return Agent(**agent_object.__dict__)


    def generate_age(self):
        return self.config.age_generator.retrieve_age()

    def generate_password(self) -> str:
        return self.config.password_generator.retrieve_password()

    def generate_profile(self) -> Profile:
        return self.config.profile_generator.retrieve_profile()

    def generate_email(self, agent: Profile) -> str:
        return self.config.mail_generator.retrieve_email(
            agent=agent
            )
    

def generate_sample_agent(maker: UserGenerator) -> Agent:
    agent_object = maker.generate()
    return agent_object
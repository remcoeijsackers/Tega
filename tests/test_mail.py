import re
from unittest import TestCase
from src.providers.age import retrieve_age_provider

from src.providers.mail import retrieve_mail_provider
from src.providers.mail.mail_generator import DisposableMail, FakeMail
from src.providers.password import retrieve_password_provider
from src.providers.profile import retrieve_profile_provider

from src.agents.user_service import UserGenerator, MakerConfig
from src.agents.user_service import generate_sample_agent


class TestMail(TestCase):

    def test_it_retrieves_the_correct_provider(self):

        test_mail_ran = retrieve_mail_provider(name="f")

        self.assertIsInstance(test_mail_ran, FakeMail)

        test_mail_ran = retrieve_mail_provider(name="d")

        self.assertIsInstance(test_mail_ran, DisposableMail)

    def test_it_generates_valid_email(self):
        def check(email):
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if (re.fullmatch(regex, email)):
                return True
            return False

        mail_handler = retrieve_mail_provider(name="f")
        profile_handler = retrieve_profile_provider()
        password_handler = retrieve_password_provider(type="r", length=20)
        age_handler = retrieve_age_provider(type="r")

        generator = UserGenerator(
            MakerConfig(
                mail_generator=mail_handler,
                profile_generator=profile_handler,
                password_generator=password_handler,
                age_generator=age_handler
            )
        )

        agent = generate_sample_agent(generator)

        self.assertEqual(check(agent.email), True)

    def test_it_generates_multiple_valid_emails(self):
        def check(email):
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if (re.fullmatch(regex, email)):
                return True
            return False

        mail_handler = retrieve_mail_provider(name="f")
        profile_handler = retrieve_profile_provider()
        password_handler = retrieve_password_provider(type="r", length=20)
        age_handler = retrieve_age_provider(type="r")

        generator = UserGenerator(
            MakerConfig(
                mail_generator=mail_handler,
                profile_generator=profile_handler,
                password_generator=password_handler,
                age_generator=age_handler
            )
        )

        agents = []
        for _ in range(20):
            agent = generate_sample_agent(generator)
            agents.append(agent)

        agent_objects = [i.to_dict() for i in agents]

        for i in agent_objects:
            self.assertEqual(check(i.get("email")), True)
            self.assertIn("@", i.get("email"))

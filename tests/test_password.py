from unittest import TestCase
from src.providers.password import retrieve_password_provider
from src.providers.password.password_generator import RandomPasswordGenerator
from src.providers.password.password_generator \
    import AlphaNumericPasswordGenerator
import re


class TestPassword(TestCase):

    @staticmethod
    def is_alpha(value):
        return bool(re.match('^[a-zA-Z0-9]+$', value))

    def test_it_retrieves_the_correct_provider(self):

        test_pw = retrieve_password_provider(type="r", length=20)

        self.assertIsInstance(test_pw, RandomPasswordGenerator)

        test_pw = retrieve_password_provider(type="a", length=20)

        self.assertIsInstance(test_pw, AlphaNumericPasswordGenerator)

    def test_the_password_generated_is_correct_format(self):

        test_pw = retrieve_password_provider(type="a", length=20)

        self.assertIsInstance(test_pw, AlphaNumericPasswordGenerator)
        pw = test_pw.retrieve_password()

        self.assertTrue(self.is_alpha(pw))

        test_pw_random = retrieve_password_provider(type="r", length=20)

        pw = test_pw_random.retrieve_password()

        self.assertFalse(self.is_alpha(pw))

    def test_the_password_generated_is_correct_length(self):

        test_pw = retrieve_password_provider(type="r", length=12)

        pw = test_pw.retrieve_password()

        self.assertEqual(len(pw), 12)
       
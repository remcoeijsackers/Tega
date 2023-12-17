from unittest import TestCase
import datetime

from src.providers.age import retrieve_age_provider
from src.providers.age.age_generator import AdultAgeGenerator
from src.providers.age.age_generator import RandomAgeGenerator
from src.providers.age.age_generator import MinorAgeGenerator


class TestAge(TestCase):

    @staticmethod
    def get_difference(date1, date2):
        delta = date2 - date1
        years = delta.days/365
        return abs(years)

    @staticmethod
    def validate(date_text):
        try:
            datetime.date.fromisoformat(date_text)
        except ValueError as e :
            raise ValueError("Incorrect data format: {}, \
            should be YYYY-MM-DD".format(e))

    def test_it_retrieves_the_correct_provider(self):

        test_age_ran = retrieve_age_provider(type="r")

        self.assertIsInstance(test_age_ran, RandomAgeGenerator)

        test_age_adult = retrieve_age_provider(type="a")

        self.assertIsInstance(test_age_adult, AdultAgeGenerator)

        test_age_minor = retrieve_age_provider(type="m")

        self.assertIsInstance(test_age_minor, MinorAgeGenerator)

    def test_the_age_generated_is_correct_format(self):

        test_age_adult = retrieve_age_provider(type="a")

        self.assertIsInstance(test_age_adult, AdultAgeGenerator)

        age = str(test_age_adult.retrieve_age().date())

        try: 
            self.validate(age)
        except Exception as e:
            self.fail(e)

        test_age_m = retrieve_age_provider(type="m")
        
        age = str(test_age_m.retrieve_age().date())

        try: 
            self.validate(age)
        except Exception as e:
            self.fail(e)

        test_age_r = retrieve_age_provider(type="r")
        
        age = str(test_age_r.retrieve_age().date())

        try: 
            self.validate(age)
        except Exception as e:
            self.fail(e)

    def test_the_age_generated_is_above_18(self):

        test_age_adult = retrieve_age_provider(type="a")

        self.assertIsInstance(test_age_adult, AdultAgeGenerator)

        age = test_age_adult.retrieve_age().date()

        now = datetime.datetime.now().date()

        diff = self.get_difference(age, now)

        self.assertGreaterEqual(diff, 18)

    def test_the_age_generated_is_below_18(self):

        test_age_minor = retrieve_age_provider(type="m")

        self.assertIsInstance(test_age_minor, MinorAgeGenerator)

        age = test_age_minor.retrieve_age().date()

        now = datetime.datetime.now().date()

        diff = self.get_difference(age, now)

        self.assertLessEqual(diff, 18)

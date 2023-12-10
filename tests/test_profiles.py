from unittest import TestCase
from src.providers.profile import retrieve_profile_provider
from src.providers.profile.profile_generator import RandomProfileGenerator, NatProfileGenerator, Profile
from src.constants.names import dutch_surnames, dutch_female_firstnames, dutch_male_firstnames

class TestProfiles(TestCase):


    def test_it_retrieves_the_correct_provider(self):
        test_profile_ran = retrieve_profile_provider()

        self.assertIsInstance(test_profile_ran, RandomProfileGenerator)

        test_profile_ran = retrieve_profile_provider(gender="f")

        self.assertIsInstance(test_profile_ran, RandomProfileGenerator)

        test_profile_nat = retrieve_profile_provider(name="Dutch")

        self.assertIsInstance(test_profile_nat, NatProfileGenerator)

        test_profile_nat = retrieve_profile_provider(name="USA", gender="m")

        self.assertIsInstance(test_profile_nat, NatProfileGenerator)

    def test_it_generates_expected_object(self):
        test_profile_ran = retrieve_profile_provider()

        test_profile = test_profile_ran.retrieve_profile()

        self.assertIsInstance(test_profile, Profile)

    def test_object_has_expected_attrs(self):
        test_profile_ran = retrieve_profile_provider()

        test_profile = test_profile_ran.retrieve_profile()

        self.assertIn("first_name", test_profile.__dict__.keys())
        self.assertIn("last_name", test_profile.__dict__.keys())
        self.assertIn("nationality", test_profile.__dict__.keys())


    def test_it_generates_mostly_unique_items(self):
        """
        Test that, for every 5 profiles generated,
        There are generally no duplicates.

        """
        test_profile_ran = retrieve_profile_provider()

        profile_names = []
        for _ in range(5):
            prof = test_profile_ran.retrieve_profile()
            name = prof.first_name + " " + prof.initial if prof.initial else "" + " " + prof.last_name
            profile_names.append(name)

        test_duplicates = set(profile_names)

        self.assertLessEqual(len(test_duplicates), len(profile_names))        


    def test_it_generates_expected_nationality_name(self):
        test_profile_nat = retrieve_profile_provider(name="Dutch")

        test_profile = test_profile_nat.retrieve_profile()

        self.assertIn(test_profile.last_name, dutch_surnames)
        self.assertIn(test_profile.first_name, dutch_male_firstnames + dutch_female_firstnames)
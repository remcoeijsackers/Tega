from unittest import TestCase
from src.constants.names import usa_surnames, usa_male_firstnames, usa_female_firstnames
from src.constants.names import get_first_based_nat, get_last_based_nat


class TestNames(TestCase):


    def test_it_returns_expected_last_name(self):
        last = get_last_based_nat(nat="USA")
        self.assertIn(last, usa_surnames)

    def test_it_returns_expected_first_name(self):
        first = get_first_based_nat(nat="USA")
        self.assertIn(first, usa_male_firstnames + usa_female_firstnames)

    def test_it_returns_expected_first_name_gender(self):
        first_f = get_first_based_nat(nat="USA", gender="f")
        self.assertIn(first_f, usa_female_firstnames)

        first_m = get_first_based_nat(nat="USA", gender="m")
        self.assertIn(first_m, usa_male_firstnames)
import re
from unittest import TestCase

from src.commands import generate_account
from src.commands.command_handler import CliAccountHandler


class TestCommands(TestCase):


    def test_it_returns_the_correct_type(self):

        args = CliAccountHandler.handle_request({})

        test_agents = generate_account(**args)

        self.assertIsInstance(test_agents, list)
        self.assertIsInstance(test_agents[0], dict)


    def test_it_returns_the_expected_values(self):
        
        args = CliAccountHandler.handle_request({})

        test_agents = generate_account(**args)

        keys = ["first_name", "last_name", "birthdate", "email", "password", "nationality", "birthdate", "age"]

        for i in keys:
            self.assertIn(i, test_agents[0])
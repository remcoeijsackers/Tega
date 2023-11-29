import datetime
import random

from src.objects.agent import Profile
from src.constants.names import last_names, letters, get_first_based_nat, get_last_based_nat, nationality

class ProfileGenerator(object):

    def retrieve_profile(self) -> Profile:
        raise NotImplementedError
    
class NatProfileGenerator(ProfileGenerator):

    @staticmethod
    def __coin_flip():
        return random.choice([True, False])
    
    @staticmethod
    def __gender():
        return random.choice(["f", "m"])

    def __generate_stub(self) -> Profile:
        i = str(random.choice(letters)).upper()

        n = random.choice(nationality)

        return Profile( **{
             "nat": n,
             "first_name": get_first_based_nat(n, self.__gender()),
             "last_name": get_last_based_nat(n),
             "initial": i if self.__coin_flip() else None,
        })

    def retrieve_profile(self):
        return self.__generate_stub()

class RandomProfileGenerator(ProfileGenerator):

    def retrieve_profile(self) -> Profile:
        raise NotImplementedError
    
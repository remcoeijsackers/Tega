import datetime
import random

from src.objects.agent import Profile
from src.constants.names import last_names, letters, get_first_based_nat, nationality

class ProfileGenerator(object):

    def retrieve_profile(self):
        raise NotImplementedError
    
class NatProfileGenerator(ProfileGenerator):

    @staticmethod
    def __coin_flip():
        return random.choice([True, False])

    def __generate_stub(self) -> Profile:
        l = random.choice(last_names)
        i = str(random.choice(letters)).upper()

        n = random.choice(nationality)

        return Profile( **{
             "nat": n,
             "first_name": get_first_based_nat(n),
             "last_name": l,
             "initial": i if self.__coin_flip() else None,
        })

    def retrieve_profile(self):
        return self.__generate_stub()

class RandomProfileGenerator(ProfileGenerator):

    def retrieve_profile(self):
        raise NotImplementedError
    
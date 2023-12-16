import datetime
import random
from dataclasses import dataclass

from src.objects.agent import Profile
from src.constants.names import letters, get_first_based_nat, get_last_based_nat
from src.constants.names import nationality as profile_nationality
from src.constants.names import female_first_names, male_first_names

class ProfileGenerator(object):

    def retrieve_profile(self) -> Profile:
        raise NotImplementedError

@dataclass
class NatProfileGenerator(ProfileGenerator):
    nationality: str
    gender: str | None = None


    @staticmethod
    def __coin_flip() -> bool:
        return random.choice([True, False])

    def __gender(self) -> str:
        if not self.gender:
            return random.choice(["f", "m"])
        else:
            return self.gender
        
    def __infer_gender_from_name(self, name):
        if name in female_first_names:
            return "f"
        if name in male_first_names:
            return "m"

    def __generate_stub(self, nation) -> Profile:
        i = str(random.choice(letters)).upper()

        n = nation

        f_name = get_first_based_nat(n, self.__gender())
        gender = self.__infer_gender_from_name(f_name)

        return Profile( **{
             "nationality": n,
             "first_name": f_name,
             "last_name": get_last_based_nat(n),
             "initial": i if self.__coin_flip() else None,
             "gender": gender
        })

    def retrieve_profile(self):
        return self.__generate_stub(self.nationality)


@dataclass
class RandomProfileGenerator(ProfileGenerator):
    gender: str | None = None

    @staticmethod
    def __coin_flip() -> bool:
        return random.choice([True, False])

    def __gender(self) -> str:
        if not self.gender:
            return random.choice(["f", "m"])
        else:
            return self.gender

    def __infer_gender_from_name(self, name):
        if name in female_first_names:
            return "f"
        if name in male_first_names:
            return "m"

    def __generate_stub(self) -> Profile:
        i = str(random.choice(letters)).upper()

        n = random.choice(profile_nationality)

        f_name = get_first_based_nat(n, self.__gender())
        gender = self.__infer_gender_from_name(f_name)

        return Profile( **{
             "nationality": n,
             "first_name": f_name,
             "last_name": get_last_based_nat(n),
             "initial": i if self.__coin_flip() else None,
             "gender": gender
        })

    def retrieve_profile(self):
        return self.__generate_stub()
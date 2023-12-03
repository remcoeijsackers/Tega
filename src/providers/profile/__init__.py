from src.objects.factory import ObjectFactory
from .profile_generator import ProfileGenerator, NatProfileGenerator, RandomProfileGenerator
from src.constants.names import nationality

class ProfileFactory(ObjectFactory):

    def retrieve_provider(self, name, gender) -> ProfileGenerator:
        if name in nationality:
            return NatProfileGenerator(
                nationality=name,
                gender=gender
            )
        if name in ["random", "r"]:
            return RandomProfileGenerator(
                gender=gender
            )
        return ProfileGenerator()

def retrieve_profile_provider(name="r", gender=None) -> ProfileGenerator:
    return ProfileFactory().retrieve_provider(name, gender)
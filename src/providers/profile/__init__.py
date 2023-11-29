from src.objects.factory import ObjectFactory
from .profile_generator import ProfileGenerator, NatProfileGenerator, RandomProfileGenerator

class ProfileFactory(ObjectFactory):

    def retrieve_provider(self, value) -> ProfileGenerator:
        if value in ["nationality",  "n"]:
            return NatProfileGenerator()
        if value in ["random", "r"]:
            return RandomProfileGenerator()
        return ProfileGenerator()

def retrieve_profile_provider(name="n") -> ProfileGenerator:
    return ProfileFactory().retrieve_provider(name)
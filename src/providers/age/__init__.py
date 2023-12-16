
from src.objects.factory import ObjectFactory
from .age_generator import RandomAgeGenerator, MinorAgeGenerator, AgeGenerator, AdultAgeGenerator

class AgeFactory(ObjectFactory):

    def retrieve_provider(self, type) -> AgeGenerator:
        if type in ["random",  "r"]:
            return RandomAgeGenerator()
        if type in ["minor", "m"]:
            return MinorAgeGenerator()
        if type in ["adult", "a"]:
            return AdultAgeGenerator()
        return AgeGenerator()

def retrieve_age_provider(type) -> AgeGenerator:
    return AgeFactory().retrieve_provider(type)
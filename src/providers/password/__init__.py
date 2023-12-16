
from src.objects.factory import ObjectFactory
from .password_generator import PasswordGenerator, RandomPasswordGenerator, AlphaNumericPasswordGenerator

class PasswordFactory(ObjectFactory):

    def retrieve_provider(self, type, length) -> PasswordGenerator:
        if type in ["random",  "r"]:
            return RandomPasswordGenerator(length)
        if type in ["alphanumeric", "a"]:
            return AlphaNumericPasswordGenerator(length)
        return PasswordGenerator(length)

def retrieve_password_provider(type, length) -> PasswordGenerator:
    return PasswordFactory().retrieve_provider(type, length)
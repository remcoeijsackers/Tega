from src.utils.passwords import generate_password

class PasswordGenerator(object):

    def __init__(self, length) -> None:
        self.length = length

    def retrieve_password(self):
        raise NotImplementedError
    

class RandomPasswordGenerator(PasswordGenerator):

    def __init__(self, length) -> None:
        self.length = length

    def retrieve_password(self):
        return generate_password(self.length)
    
class AlphaNumericPasswordGenerator(PasswordGenerator):

    def __init__(self, length) -> None:
        self.length = length

    def retrieve_password(self):
        return generate_password(self.length, punctuation=False)
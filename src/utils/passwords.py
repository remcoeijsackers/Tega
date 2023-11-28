import string
import secrets

def __random_string(length: int, **kwargs):
    """
    Generates a random string.

    optional Kwargs:
        lowercase = True/False
        punctuation = True/False
    """
    characters = string.ascii_uppercase + string.digits

    if 'lowercase' in kwargs and kwargs['lowercase'] == True:
        characters += string.ascii_lowercase 

    if 'punctuation' in kwargs and kwargs['punctuation'] == True:
        characters += string.punctuation
        
    passwordStub = secrets.choice(string.ascii_uppercase)
    passwordStub += secrets.choice(string.digits)
    passwordStub += secrets.choice(string.digits)

    if 'lowercase' in kwargs and kwargs['lowercase'] == True:
        passwordStub += secrets.choice(string.ascii_lowercase)

    if 'punctuation' in kwargs and kwargs['punctuation'] == True:
        characters += secrets.choice(string.punctuation)

    for _ in range(length - 4):
        passwordStub += secrets.choice(characters)

    passwordList = list(passwordStub)

    secrets.SystemRandom().shuffle(passwordList)

    return ''.join(passwordList)


def generate_password(chars: int =20):
        """
        Generates a password with at least one uppercase,
        one lowercase, one digit, and one punctuation.
        """
        return __random_string(chars, lowercase=True, punctuation=True)

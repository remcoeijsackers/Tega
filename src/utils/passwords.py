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
        
    pass_stub = secrets.choice(string.ascii_uppercase)
    pass_stub += secrets.choice(string.digits)
    pass_stub += secrets.choice(string.digits)

    if 'lowercase' in kwargs and kwargs['lowercase'] == True:
        pass_stub += secrets.choice(string.ascii_lowercase)

    if 'punctuation' in kwargs and kwargs['punctuation'] == True:
        characters += secrets.choice(string.punctuation)

    for _ in range(length - 4):
        pass_stub += secrets.choice(characters)

    password_parts = list(pass_stub)

    secrets.SystemRandom().shuffle(password_parts)

    return ''.join(password_parts)


def generate_password(chars: int =20):
        """
        Generates a password with at least one uppercase,
        one lowercase, one digit, and one punctuation.
        """
        return __random_string(chars, lowercase=True, punctuation=True)

from src.commands.handler.command_handler import RequestHandler
from src.constants.names import nationality

flaskAccountHandler = RequestHandler(
         defined_args={
            "mail": {
                 "default": "clean",
                 "supported": ["c", "f", "clean", "fake"]
            }, 
            "email_type": {
                "default":  "gmail.com",
                "supported": ["*c"]
            },
            "nationality": {
                 "default":  "random",
                 "supported": ["r", "random"] + nationality
            },
            "gender": {
                "default": "random",
                "supported": ["m", "f", "r", "male", "female", "random"]
            },
            "count": {
                "default": 1,
                "supported": ["*i"]
            }, 
            "logging": {
                "default": "none",
                "supported": ["pretty", "verbose", "none"]
            },
            "password": {
                 "default": "alphanumeric",
                 "supported": ["r", "a", "random", "alphanumeric"]
            },
            "password_length": {
                 "default": 20,
                 "supported": ["*i"]
            },
            "age": {
                 "default": "random",
                 "supported": ["r", "m", "a", "random", "minor", "adult"]
            }
         }
)

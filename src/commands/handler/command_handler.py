import logging
import re

logger = logging.getLogger(__name__)

class RequestHandler():
    def __init__(self, defined_args) -> None:
        self.args: None
        self.defined_args: dict = defined_args

    def __arg_present(self, name):
        value = self.args.get(name)
        
        if value == None:
            return False

        return True

    def __read_wildcards(self, name):
        rule = self.defined_args.get(name).get("supported")
        value = self.args.get(name)

        if str(value) in rule:
            return True
        if rule[0] == "*":
            return True
        if rule[0] == "*c" and isinstance(value, str):
            return True
        if rule[0] == "*i":
            match = re.match(
                "^[-+]?[0-9]+$",
                str(value)
            )
            if match:
                return True

        return False

    def __arg_allowed(self, name):
        return self.__read_wildcards(name)

    def __retrieve(self, name):
        # if the checked value is not in proved args
        # it should take the default.
        if not self.__arg_present(name):
            return self.defined_args.get(name).get("default")

        if not self.__arg_allowed(name):
            return self.defined_args.get(name).get("default")

        return self.args.get(name)
    
    def update_defined_arg(self, key:str, value: dict):
        self.defined_args[key]= value
        return self

    def handle_request(self, args) -> dict:
        self.args = args
        data = {str(i): self.__retrieve(i) for i in self.defined_args.keys()} 

        return data



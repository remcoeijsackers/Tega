import datetime
import json

from ..utils.format import remove_null


class Profile():
    def __init__(self, **kwargs) -> None:
        self.first_name = kwargs.get("first_name",None)
        self.last_name = kwargs.get("last_name",None)
        self.initial = kwargs.get("initial", None)
        self.birthdate: datetime.datetime | None = kwargs.get("age", None)
        self.email =kwargs.get("email", None)
        self.password =kwargs.get("password", None)
        self.nat = kwargs.get("nat", None)

class Agent(Profile):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @property
    def age(self):
        x = datetime.datetime.now().date() - datetime.datetime.fromisoformat(str(self.birthdate)).date()
        yold = x/365
        return yold.days
    
    @property
    def date_of_birth(self):
        if isinstance(self.birthdate, datetime.datetime):
            return str(self.birthdate.date())
        else:
            return self.birthdate
    
    def name(self):
        return f"{self.first_name} {self.initial if self.initial else ''}{' ' if self.initial else ''}{self.last_name}"

    def to_json(self) -> json:
        
        d = self.__dict__

        d["age"] = self.age
        d["birthdate"] = self.date_of_birth

        cleaned = remove_null(d)
  
        json_formatted_str = json.dumps(cleaned, indent=2)
        return json_formatted_str

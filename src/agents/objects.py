import datetime
import json

class AgentStub():
    def __init__(self, **kwargs) -> None:
        self.first_name = kwargs.get("first_name",None)
        self.last_name = kwargs.get("last_name",None)
        self.initial = kwargs.get("initial", None)
        self.birthdate: datetime.datetime | None = kwargs.get("age", None)
        self.email =kwargs.get("email", None)
        self.password =kwargs.get("password", None)
        self.nat = kwargs.get("nat", None)

class Agent(AgentStub):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @property
    def age(self):
        x = datetime.datetime.now().date() - datetime.datetime.fromisoformat(self.birthdate).date()
        yold = x/365
        return yold.days
    
    def name(self):
        return f"{self.first_name} {self.initial if self.initial else ''}{' ' if self.initial else ''}{self.last_name}"

    def to_json(self):
        self.birthdate = str(self.birthdate)
        d = self.__dict__
        d["age"]= self.age
        return json.dumps(d)

    def intro(self):
        "print the agents description"
        print(self.name())
        print(self.nat)
        print(self.age)
        print(f"{self.birthdate.date()}")
        print(self.email)
        print(self.password)
        print("\n")
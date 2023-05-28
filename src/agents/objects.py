import datetime

class AgentStub():
    def __init__(self, **kwargs) -> None:
        self.first_name = kwargs.get("first_name",None)
        self.last_name = kwargs.get("last_name",None)
        self.initial = kwargs.get("initial", None)
        self.age: datetime.datetime | None = kwargs.get("age", None)
        self.email =kwargs.get("email", None)
        self.password =kwargs.get("password", None)
        self.nat = kwargs.get("nat", None)

class Agent(AgentStub):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
    
    def name(self):
        return f"{self.first_name} {self.initial if self.initial else ''}{' ' if self.initial else ''}{self.last_name}"

    def intro(self):
        print(self.name())
        print(self.nat)
        x = datetime.datetime.now().date() - self.age.date()
        yold = x/365
        print(f"{self.age.date()} ({yold.days})")
        print(self.email)
        print(self.password)
        print("\n")
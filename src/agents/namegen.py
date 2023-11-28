import random
import datetime

from .objects import Agent, AgentStub
from .constants import male_first_names, last_names, letters, chars, get_first_based_nat,nationality

class MakerSettings:
    def __init__(self, store: bool) -> None:
        self.email_type = "@gmail.com"
        self.password_type = "all" # all | no_special
        self.store = store


class Maker:
    def __init__(self, settings: MakerSettings) -> None:
        self.settings = settings

    def generate(self, options: list or None = None):
        st = self.__generate_stub()
        st.age = self.__generate_age()
        st.email = self.__generate_email(st)
        st.password = self.__generate_password(st)
        
        return Agent(**st.__dict__)

    @staticmethod
    def coin_flip():
        return random.choice([True, False])

    def __generate_stub(self) -> AgentStub:
        l = random.choice(last_names)
        i = str(random.choice(letters)).upper()

        n = random.choice(nationality)
        return AgentStub( **{
             "nat": n,
             "first_name": get_first_based_nat(n),
             "last_name": l,
             "initial": i if self.coin_flip() else None,

        })
    
    @staticmethod
    def __generate_age():
        y = random.randrange(1980, 2001)
        m = random.randrange(1,12)
        d = random.randrange(1,27)
        return datetime.datetime(y,m,d)

    def __generate_email(self, agent: AgentStub):
        def __r_first(f):
            op = [str(f).lower(), str(f), f"{random.randrange(0, 100)}{str(f).lower()}"]
            return random.choice(op)
        
        def __r_sec(s):
            op = [s.year, f"{s.year}.{s.month}", f"{str(s.year)[2:]}"]
            return random.choice(op)

        def __r_third(l):
            op = [str(l.last_name)[0:1], f".{str(l.last_name)[0:1]}", str(l.last_name), str(l.last_name).lower()]
            if l.initial != None:
                op.append(f"{str(l.initial).upper()}.{str(l.last_name)}")
                op.append(f"{str(l.initial).upper()}.{str(l.last_name)[0:1]}")
            return random.choice(op)

        pi = f"{__r_first(agent.first_name)}{__r_sec(agent.age)}{__r_third(agent)}"
        return f"{pi}{self.settings.email_type}"
    
    @staticmethod
    def __generate_password(agent: AgentStub):
        def gL():
            l = random.choice(letters)
            op = [str(l).upper(), l]
            return random.choice(op)
        def gN():
            return random.randint(0,10000)
        def gC():
            return random.choice(chars)
        
        def get_pw(l: int):
            op = [gL(), gN(), gC()]
            p = ""
            for _ in range(l):
                p += str(random.choice(op))
            return p 
        pw = f"{gN()}{gC()}{get_pw(10)}{gL()}"
        return pw

def generate_sample_agent(maker: Maker) -> Agent:
    ag = maker.generate()
    return ag
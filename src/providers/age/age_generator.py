import random
import datetime

class AgeGenerator(object):

    def __init__(self) -> None:
        pass

    def retrieve_age(self,):
        raise NotImplementedError

class RandomAgeGenerator(AgeGenerator):

    def __init__(self) -> None:
        self.currentyear = datetime.datetime.now().year

    def __generate_age(self):
        y = random.randrange(1900, self.currentyear)
        m = random.randrange(1,12)
        d = random.randrange(1,27)
        return datetime.datetime(y,m,d)


    def retrieve_age(self):
        return self.__generate_age()

class MinorAgeGenerator(AgeGenerator):

    def __generate_age(self):
        end_date = datetime.date.today().replace(year=datetime.date.today().year - 5)
        start_date = datetime.date.today().replace(year=datetime.date.today().year - 18)
        date_range = range(start_date.toordinal(), end_date.toordinal())
        random_dates = [datetime.date.fromordinal(o) for o in random.sample(date_range, 10)]

        age: datetime.date = random.choice(random_dates)
        return datetime.datetime(age.year, age.month, age.day)


    def retrieve_age(self):
        return self.__generate_age()

class AdultAgeGenerator(AgeGenerator):

    def __generate_age(self):
        end_date = datetime.date.today().replace(year=datetime.date.today().year - 19)
        start_date = datetime.date.today().replace(year=datetime.date.today().year - 100)
        date_range = range(start_date.toordinal(), end_date.toordinal())
        random_dates = [datetime.date.fromordinal(o) for o in random.sample(date_range, 10)]

        age: datetime.date = random.choice(random_dates)
        return datetime.datetime(age.year, age.month, age.day)


    def retrieve_age(self):
        return self.__generate_age()
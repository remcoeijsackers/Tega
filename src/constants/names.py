import random 

# Surnames

usa_surnames = [
    "Smith",
    "Johnson",
    "Williams",
    "Brown",
    "Jones",
    "Miller",
    "Davis",
    "Wilson",
    "Anderson",
    "Taylor",
]

indian_surnames = [
    "Acharya",
    "Anand",
    "Anthony",
    "Arya",
    "Azad",
    "Babu",
    "Bakshi",
    "Balakrishnan"
]

newzealand_surnames = [
    "Adams",
    "Ahnau",
	"Aldous",
	"Alexander"
]

dutch_surnames = [
    "De Jong",
    "Jansen",
    "De Vries",
    "Bakker",
    "De Wit",
    "Klaasen"
]

england_surnames = [
    "Jones",
    "Williams",
    "Taylor",
    "Brown",
    "Davies",
    "Evans",
    "Thomas"
]

german_surnames = [
    "Muller",
    "Schmidt",
    "Schneider",
    "Fischer",
    "Weber",
    "Schafer",
    "Meyer",
    "Wagner"
]

turkey_surnames = [
    "Akbas",
    "Aksoy",
    "Avci",
    "Aydin",
    "Demir",
    "Demirci",
    "Kaplan",
]

french_surnames = [
    "Bernard",
    "Robert",
    "Richard",
    "Durand",
    "Dubois",
    "Moreau",
    "Simon"
]

phillippines_surnames = [
    "dela Cruz",
    "Garcia",
    "Reyes",
    "Ramos",
    "Mendoza",
    "Santos",
    "Flores",
    "Gonzales"
]

australian_surnames = [
    "Smith",
    "Jones",
    "Williams",
    "Brown",
    "Wilson",
    "Taylor",
    "Johnson",
    "Lee",
]

# First Names

usa_male_firstnames = [
    "James",
    "John",
    "Robert",
    "Michael",
    "William",
    "David",
    "Richard",
    "Charles"
]

usa_female_firstnames = [
    "Olivia",
    "Emma",
    "Charlotte",
    "Amelia",
    "Sophia",
    "Isabella",
    "Ava",
    "Mia"
]

australia_male_firstnames = [
    'Jack',
    'James',
    'Lachlan',
    'Benjamin',
    'Joshua',
    'Ryan',
    'John',
    'Patrick',
    'Samuel',
    'William'
]

australia_female_firstnames = [
    "Charlotte",
    "Ava",
    "Harper",
    "Willow",
    "Isla",
    "Olivia"
]

newzealand_female_firstnames = [
    "Mary",
    "Margaret",
    "Elizabeth",
    "Sarah",
    "Patricia",
    "Catherine",
    "Susan",
    "Helen",
    "Emma"
]

newzealand_male_firstnames = [
    'Joshua',
    'Jack',
    'Benjamin',
    'Samuel',
    'Daniel',
    'Jacob',
    'Ethan',
    'James',
    'Thomas',
    'Matthew'
]

french_female_firstnames = [
    "Chloe",
    "Salome",
    "Lea",
    "Manon",
    "Juliette",
    "Camille"
]

french_male_firstnames = [
    "Eliott",
    "Lyam",
    "Mylan",
    "Gabriel",
    "Theo"
]
england_female_firstnames = [
    "Olivia",
    "Amelia",
    "Isla",
    "Ivy",
    "Freya",
    "Lily",
    "Florence"
]

england_male_firstnames = [
    "George",  
    "Arthur",
    "Leo",
    "Harry",
    "Oscar"
]

indian_female_firstnames = [
    "Amulya",
    "Aniya",
    "Anushka",
    "Aria",
    "Ayla",
    "Devina",
    "Divya",
    "Eesha",
    "Farida",
]

indian_male_firstnames = [
    "Arjun",
    "Aum",
    "Ishan",
    "Krish",
    "Moksh",
    "Nitin",
    "Parin",
    "Rishi",
    "Shankar",
    "Veer"
]

turkey_female_firstnames = [
    "Aiyla",
    "Alara",
    "Aylin",
    "Aysun",
    "Beste",
    "Burcu",
    "Defne",
    "Ece"
]

turkey_male_firstnames = [
    "Mehmet",
    "Yusuf",
    "Furkan", 
    "Mustafa",
    "Emre"
]

phillippines_male_firstnames = [
    'Michael',
    'Ronald',
    'Ryan',
    'Joseph',
    'Joel', 
    'Jeffrey',
    'Marlon',
    'Richard',
    'Noel',
    'Jonathan'
]

phillippines_female_firstnames = [
    "Althea",
    "Andrea",
    "Angela",
    "Jasmine",
    "Kristine",
    "Nathalie",
]

dutch_male_firstnames = [
    'Liam',
    'Lucas',
    'Daan',
    'Finn',
    'Levi',
    'James',
    'Tom',
    'Luuk',
    'Jasper',
    'Henk'
]

dutch_female_firstnames = [
    'Emma',
    'Julia',
    'Mila',
    'Tess',
    'Sophie',
    'Zoe',
    'Sara',
    'Nora'
]

german_male_firstnames = [
    'Ernst',
    'Friedrich',
    'Hans',
    'Heinrich',
    'Hermann',
    'Karl',
    'Otto',
    'Paul',
    'Walter', 
    'Wilhelm'
]

german_female_firstnames = [
    'Anna',
    'Hannah',
    'Julia',
    'Lara',
    'Laura',
    'Lea',
    'Lena',
    'Lisa',
    'Michelle',
    'Sarah'
]

nationality = [
    "Dutch",
    "Australia",
    "New Zealand",
    "Philippines",
    "Turkey",
    "France",
    "USA",
    "England",
    "Germany",
    "India"
]

# All names

male_first_names = dutch_male_firstnames + australia_male_firstnames \
                    + newzealand_male_firstnames \
                    + phillippines_male_firstnames \
                    + turkey_male_firstnames + french_male_firstnames \
                    + usa_male_firstnames + england_male_firstnames \
                    + german_male_firstnames + indian_male_firstnames

female_first_names = dutch_female_firstnames + australia_female_firstnames \
                    + newzealand_female_firstnames \
                    + phillippines_female_firstnames \
                    + turkey_female_firstnames + french_female_firstnames \
                    + usa_female_firstnames + england_female_firstnames \
                    + german_female_firstnames + indian_female_firstnames

last_names = dutch_surnames + australian_surnames \
            + newzealand_surnames + phillippines_surnames \
            + turkey_surnames + french_surnames \
            + usa_surnames + england_surnames \
            + german_surnames + indian_surnames

letters = "abcdefghijlkmnoptuvw"

chars = "!@#$%^&*"


def get_last_based_nat(nat : str) -> str:
    if nat == "Turkey":
        return random.choice(turkey_surnames)
    if nat == "New Zealand":
        return random.choice(newzealand_surnames)
    if nat == "Dutch":
        return random.choice(dutch_surnames)
    if nat == "Philippines":
        return random.choice(phillippines_surnames)
    if nat == "Australia":
        return random.choice(australian_surnames)
    if nat == "USA":
        return random.choice(usa_surnames)
    if nat == "India":
        return random.choice(indian_surnames)
    if nat == "England":
        return random.choice(england_surnames)
    if nat == "Germany":
        return random.choice(german_surnames)
    if nat == "France":
        return random.choice(french_surnames)
    return random.choice(last_names)
    

def get_first_based_nat(nat : str, gender : str = "") -> str:

    if nat == "France":
        if gender == "m":
            return random.choice(french_male_firstnames)
        if gender == "f":
            return random.choice(french_female_firstnames)
        return random.choice(french_female_firstnames + french_male_firstnames)

    if nat == "Germany":
        if gender == "m":
            return random.choice(german_male_firstnames)
        if gender == "f":
            return random.choice(german_female_firstnames)
        return random.choice(german_female_firstnames + german_male_firstnames)

    if nat == "Dutch":
        if gender == "m":
            return random.choice(dutch_male_firstnames)
        if gender == "f":
            return random.choice(dutch_female_firstnames)
        return random.choice(dutch_male_firstnames + dutch_female_firstnames)

    if nat == "USA":
        if gender == "m":
            return random.choice(usa_male_firstnames)
        if gender == "f":
            return random.choice(usa_female_firstnames)
        return random.choice(usa_male_firstnames + usa_female_firstnames)
 
    if nat == "Australia":
        if gender == "m":
            return random.choice(australia_male_firstnames)
        if gender == "f":
            return random.choice(australia_female_firstnames)
        return random.choice(
            australia_male_firstnames + australia_male_firstnames
            )

    if nat == "India": 
        if gender == "m":
            return random.choice(indian_male_firstnames)
        if gender == "f":
            return random.choice(indian_female_firstnames)
        return random.choice(indian_male_firstnames + indian_female_firstnames)

    if nat == "England":
        if gender == "m":
            return random.choice(england_female_firstnames)
        if gender == "f":
            return random.choice(england_female_firstnames)
        return random.choice(
            england_female_firstnames + england_male_firstnames
            )

    if nat == "New Zealand":
        if gender == "m":
            return random.choice(newzealand_male_firstnames)
        if gender == "f":
            return random.choice(newzealand_female_firstnames)
        return random.choice(
            newzealand_female_firstnames + newzealand_male_firstnames
            )

    if nat == "Philippines":
        if gender == "m":
            return random.choice(phillippines_male_firstnames)
        if gender == "f":
            return random.choice(phillippines_female_firstnames)
        return random.choice(
            phillippines_male_firstnames + phillippines_female_firstnames
            )

    if nat == "Turkey":
        if gender == "m":
            return random.choice(turkey_male_firstnames)
        if gender == "f":
            return random.choice(turkey_female_firstnames)
        return random.choice(turkey_male_firstnames + turkey_female_firstnames)
    
    # Nationality not given

    if gender == "m":
        return random.choice(male_first_names)
    if gender == "f":
        return random.choice(female_first_names)
    
    return random.choice(male_first_names + female_first_names)

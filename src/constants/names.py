import random 

male_first_names = [
"Liam",
"Noah",
"Oliver",
"James",
"Elijah",
"William",
"Henry",
"Lucas",
"Benjamin",
"Theodore",
"Jack",
"Jimmy",
"Ben",
"Kevin",
"Mark"
]

last_names = [
"Smith",
"Johnson",
"Williams",
"Brown",
"Jones",
"Garcia",
"Miller",
"Davis",
"Baker",
"Black"
]

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

australia_male_firstnames = ['Jack', 'James', 'Lachlan', 'Benjamin', 'Joshua', 'Ryan', 'John', 'Patrick', 'Samuel', 'William']

newzealand_male_firstnames = ['Joshua', 'Jack', 'Benjamin', 'Samuel', 'Daniel', 'Jacob', 'Ethan', 'James', 'Thomas', 'Matthew']

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

phillippines_male_firstnames = ['Michael', 'Ronald', 'Ryan', 'Joseph', 'Joel', 'Jeffrey', 'Marlon', 'Richard', 'Noel', 'Jonathan']

nationality = [
    "Dutch",
    "Australia",
    "New Zealand",
    "Philippines",
    "Turkey",
    "France",
    "USA",
    "England",
    "Germany"
]

letters= "abcdefghijlkmnop"

chars = "!@#$%^&*"

def get_last_based_nat(nat:str):
    if nat == "USA":
        return random.choice(usa_surnames)
    if nat == "indian":
        return random.choice(indian_surnames)
    return random.choice(last_names)
    

def get_first_based_nat(nat:str, gender:str =""):

    if nat == "USA":
        if gender == "m":
            return random.choice(usa_male_firstnames)
        if gender == "f":
            return random.choice(usa_female_firstnames)
        return random.choice(usa_male_firstnames + usa_female_firstnames)

    if nat == "Australia":
        return random.choice(australia_male_firstnames)

    if nat == "India": 
        if gender == "m":
            return random.choice(indian_male_firstnames)
        if gender == "f":
            return random.choice(indian_female_firstnames)
        return random.choice(indian_male_firstnames + indian_female_firstnames)

    if nat == "New Zealand":
        return random.choice(newzealand_male_firstnames)

    if nat == "Philippines":
        return random.choice(phillippines_male_firstnames)

    if nat == "Turkey":
        return random.choice(str("Mehmet Yusuf Furkan Mustafa Emre").split(" "))
    else:
        return random.choice(male_first_names)
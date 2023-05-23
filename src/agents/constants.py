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

def get_first_based_nat(nat:str):

    if nat == "Australia":
        return random.choice(str("Jack James Lachlan Benjamin Joshua Ryan John Patrick Samuel William").split(" "))

    if nat == "India": 
        return random.choice(["Karna",	"Surya",	"Rama",	"Aarav",	"Vivaan",	"Krishna",	"Muhammed",	"Aryan",	"Lakhan",	"Jack"])

    if nat == "New Zealand":
        return random.choice(str("Joshua Jack Benjamin Samuel Daniel Jacob Ethan James Thomas Matthew").split(" "))

    if nat == "Philippines":
        return random.choice(str("Michael Ronald Ryan Joseph Joel Jeffrey Marlon Richard Noel Jonathan").split(" "))

    if nat == "Turkey":
        return random.choice(str("Mehmet Yusuf Furkan Mustafa Emre").split(" "))
    else:
        return random.choice(male_first_names)
[![Tega](https://github.com/remcoeijsackers/namegen/actions/workflows/python-app.yml/badge.svg)](https://github.com/remcoeijsackers/namegen/actions/workflows/python-app.yml)

# Tega
Generate fake accounts for testing.

## Usage

Start the service
```sh
make up
```

Call the service

_http://localhost:9000/_?count=2&nationality=USA

```json
{
  "accounts": [
    {
      "age": 11,
      "birthdate": "2012-08-21",
      "email": "ava.J.Wilson12@gmail.com",
      "first_name": "Ava",
      "gender": "f",
      "initial": "J",
      "last_name": "Wilson",
      "nationality": "USA",
      "password": "IiQVx6p850kECoIrBjF0"
    },
    {
      "age": 87,
      "birthdate": "1936-05-11",
      "email": "Olivia.N.Anderson1936@gmail.com",
      "first_name": "Olivia",
      "gender": "f",
      "initial": "N",
      "last_name": "Anderson",
      "nationality": "USA",
      "password": "rl44Xog3Erk7gP3fleYn"
    }
  ],
  "config": {
    "age": "random",
    "count": "2",
    "email_type": "gmail.com",
    "gender": "random",
    "logging": "none",
    "mail": "clean",
    "nationality": "USA",
    "password": "alphanumeric",
    "password_length": 20
  }
}
```

URL params

* count
    - default: 1
    - supported: any int
* age
    - default: "random"
    - supported: "random", "minor", "adult"
* mail
    - default: "clean"
    - supported: "clean", "fake"
* email_type
    - default:  "gmail.com"
    - supported: any string
* nationality
    - default:  "random",
    - supported: "random" + nationality
* gender
    - default: "random",
    - supported": "male", "female", "random"
* password
    - default: "alphanumeric",
    - supported": "random", "alphanumeric"
* password_length
    - default: 20
    - supported: any int


## Supported nationalities

The following nationalities have their most common first and lastnames present in [the project](src/constants/names.py).

* "Dutch"
* "Australia"
* "New Zealand"
* "Philippines"
* "Turkey"
* "France"
* "USA"
* "England"
* "Germany"
* "India"

Use them to retrieve accounts based on the nationality.

_http://localhost:9000/_?count=3&nationality=USA&gender=f&age=adult

```json
{
  "accounts": [
    {
      "age": 81,
      "birthdate": "1942-05-22",
      "email": "Sophia1942@gmail.com",
      "first_name": "Sophia",
      "gender": "f",
      "last_name": "Jones",
      "nationality": "USA",
      "password": "q6C0qxYk56wcPGXJH7xu"
    },
    {
      "age": 83,
      "birthdate": "1940-05-13",
      "email": "Amelia1940@gmail.com",
      "first_name": "Amelia",
      "gender": "f",
      "initial": "F",
      "last_name": "Taylor",
      "nationality": "USA",
      "password": "XgNQWqoyMgR5214qVT3J"
    },
    {
      "age": 61,
      "birthdate": "1962-08-27",
      "email": "Amelia1962@gmail.com",
      "first_name": "Amelia",
      "gender": "f",
      "last_name": "Smith",
      "nationality": "USA",
      "password": "K0SIeuHeCOVz7KLpa2e1"
    }
  ],
  "config": {
    "age": "adult",
    "count": "3",
    "email_type": "gmail.com",
    "gender": "f",
    "logging": "none",
    "mail": "clean",
    "nationality": "USA",
    "password": "alphanumeric",
    "password_length": 20
  }
}
```
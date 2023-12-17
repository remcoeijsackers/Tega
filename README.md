<p align="center">
  <a href="#"><img src="assets/images/logo.jpg" style="width:50%"/></a>
</p>

<p align="center">
A development tool to generate random fake accounts, based on a number of parameters.
</p>

<p align="center">
    <a href="https://github.com/remcoeijsackers/namegen/actions/workflows/python-app.yml">
        <img alt="CI Workflow" src="https://github.com/remcoeijsackers/tega/actions/workflows/python-app.yml/badge.svg"
        >
    </a>
    <a href="#">
        <img alt="Python" src="https://img.shields.io/static/v1?label=Python&message=3.11%2B&color=informational&logo=python">
    </a>
</p>

## Main Features
- Easily generate fake accounts trough a docker service / cli
- Specify types of accounts through URL params


## Getting started

### Prerequesites
- Docker
- Make

### Starting the service
1. Open your terminal and run `make up`
2. call `http://localhost:9000/` to start generating accounts.

## Supported params

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


## Usage

### Example requests

`generate nationatility based accounts`

http://localhost:9000/?count=2&nationality=USA

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

`generate USA based accounts, above 18 years, gender female`

http://localhost:9000/?count=3&nationality=USA&gender=f&age=adult

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

`generate random accounts, above 18 years, gender male`

http://localhost:9000/?count=3&gender=m&age=adult

```json
{
  "accounts": [
    {
      "age": 31,
      "birthdate": "1992-04-01",
      "email": "otto1992@gmail.com",
      "first_name": "Otto",
      "gender": "m",
      "last_name": "Fischer",
      "nationality": "Germany",
      "password": "WdCzo629b5fInInZo3H8"
    },
    {
      "age": 62,
      "birthdate": "1961-07-25",
      "email": "mustafa1961@gmail.com",
      "first_name": "Mustafa",
      "gender": "m",
      "last_name": "Demir",
      "nationality": "Turkey",
      "password": "TC5hBiOKJIaNw1Pd0yrF"
    },
    {
      "age": 66,
      "birthdate": "1957-09-12",
      "email": "Theo1957@gmail.com",
      "first_name": "Theo",
      "gender": "m",
      "last_name": "Robert",
      "nationality": "France",
      "password": "1Mjhb2w68vO5l2E82tg3"
    }
  ],
  "config": {
    "age": "adult",
    "count": "3",
    "email_type": "gmail.com",
    "gender": "m",
    "logging": "none",
    "mail": "clean",
    "nationality": "random",
    "password": "alphanumeric",
    "password_length": 20
  }
}

```
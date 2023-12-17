from dataclasses import dataclass


@dataclass
class RequestConfig():
    logging: str


@dataclass
class AccountRequestConfig(RequestConfig):
    mail: str
    email_type: str
    nationality: str
    gender: str
    count: int
    password: str
    password_length: int
    age: str
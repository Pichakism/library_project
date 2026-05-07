from enum import Enum

class Book_Status(Enum):
    AVAILABE = 1
    UNAVAILABLE = 2
    ON_LOAN = 3
    RESERVED = 4

class Member_Status(Enum):
    AVAILABE = 1
    UNAVAILABLE = 2

class Digital_version(Enum):
    YES = 1
    NO = 2

class Physical_version(Enum):
    YES = 1
    NO = 2
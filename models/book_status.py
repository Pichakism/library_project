from enum import Enum

class Book_Status(Enum):
    AVAILABE = 1
    UNAVAILABLE = 2
    ON_LOAN = 3
    RESERVED = 4
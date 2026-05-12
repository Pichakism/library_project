from enum import Enum
class Book_Status(Enum):
    # Enum representing book status types
    # - Used to standardize book availability states
    AVAILABE = 1
    UNAVAILABLE = 2
    ON_LOAN = 3
    RESERVED = 4

class Member_Status(Enum):
    # Enum representing member status types
    # - Defines whether a member is active or not
    AVAILABE = 1
    UNAVAILABLE = 2

class Digital_version(Enum):
    # Enum representing digital availability of a book
    # - Specifies if a digital version exists
    YES = 1
    NO = 2

class Physical_version(Enum):
    # Enum representing physical availability of a book
    # - Specifies if a physical copy exists
    YES = 1
    NO = 2

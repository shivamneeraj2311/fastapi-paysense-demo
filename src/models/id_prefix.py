import enum

class IdPrefix(str, enum.Enum):
    NONE = ""
    DUMMY_USER = "user"
    DUMMY_ORG = "org"
# Contains phone information

class Phone:
    # Constructor
    def __init__(self, phone: str, phone_type: str):
        self.__phone = phone
        self.__type = phone_type

    # Setters

    def set_number(self, phone: str):
        self.__phone = phone

    def set_type(self, phone_type: str):
        self.__type = phone_type

    # Getters

    def get_number(self):
        return self.__phone

    def get_type(self):
        return self.__type

    # String override
    def __str__(self):
        return f"{self.__phone} ({self.__type})"
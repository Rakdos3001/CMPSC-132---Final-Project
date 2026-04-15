# Contains a physical address

class MailingAddress:
    # Constructor
    def __init__(self, street_address: str, city: str, state: str, zip_code: int, address_type: str):
        self.__street_address = street_address
        self.__city = city
        self.__state = state
        self.__zip = zip_code
        self.__address_type = address_type

    # Setters
    def set_street_address(self, street: str):
        self.__street_address = street

    def set_city(self, city: str):
        self.__city = city

    def set_state(self, state: str):
        self.__state = state

    def set_zip(self, zip_code: str):
        self.__zip = zip_code

    def set_address_type(self, address_type: str):
        self.__address_type = address_type

    # Getters
    def get_street_address(self):
        return self.__street_address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip_code(self):
        return self.__zip

    def get_address_type(self):
        return self.__address_type

    # String overload
    def __str__(self):
        return f"{self.__street_address}, {self.__city}, {self.__state}, {self.__zip} ({self.__address_type})"

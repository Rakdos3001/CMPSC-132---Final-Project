# A date

class Date:
    # Constructor
    def __init__(self, year: int, month: int, day: int):
        self.__year = year
        self.__month = month
        self.__day = day

    # Setters

    def set_year(self, year: int):
        self.__year = year

    def set_month(self, month: int):
        self.__month = month

    def set_day(self, day: int):
        self.__day = day

    # Getters

    def get_year(self):
        return self.__year

    def get_month(self):
        return self.__month

    def get_day(self):
        return self.__day

    # String Overload
    def __str__(self):
        return f"{self.__month}/{self.__day}/{self.__year}"
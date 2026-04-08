# Course class
class Advisor:
    #Constructor
    def __init__(name_first: str, name_last: str, name_middle:str, advisor_title:str,
                 department:str, advisees: LinkedList = None):
        self.__name_first = name_first
        self.__name_last = name_last
        self.__name_middle = name_middle
        self.__advisor_title = advisor_title
        self.__department = department
        self.__advisees = advisees


    #Name Setter/Getetrs
    def set_name_first(self, name_first: str):
        self.__name_first = name_first

    def set_name_last(self, name_last: str):
        self.__name_last = name_last

    def set_name_middle(self, name_middle: str):
        self.__name_middle = name_middle

    def get_name_first(self):
        return self.__name_first

    def get_name_last(self):
        return self.__name_last

    def get_name_middle(self):
        return self.__name_middle

    #Advisor Title Setter/Getter
    def set_advisor_title(self, new_advisor_title: str):
        self.__advisor_title = new_advisor_title

    def get_advisor_title(self):
        return self.__advisor_title

    # Department Setter/Getter
    def set_department(self, new_department: str):
        self.__department = new_department

    def get_department(self):
        return self.__department

    #Advisees Setter/Getter

    self.__advisees = advisees
    def set_status(self, new_status: str):
        self.__status = new_status

    def set_advisees(self, new_advisees):
        self.__advisees = new_advisees

    def get_advisees(self):
        return self.__advisees

    def __str__(self):
        return (f"Name:{self.__name_first} {self.__name_last},{self.__name_middle} "
                f"Advisor Title: {self.__advisor_title}"
                f"Department: {self.__department}"
                f"Advisee: {advisee_str}")

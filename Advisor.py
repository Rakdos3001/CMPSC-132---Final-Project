from Person import Person
from MailingAddress import MailingAddress
from Phone import Phone
from Date import Date
from EmailAddress import EmailAddress
from Course import Course
from LinkedList import LinkedList

# Course class
class Advisor(Person):
    #Constructor
    def __init__(self, advisor_id: int, name_first: str, name_last: str, name_middle: str = None,
                 address: MailingAddress = None, emails: list[EmailAddress] = None, phones: list[Phone] = None, birth_date: Date = None,
                 advisor_title: str = None, department: str = None, advisees: LinkedList = None):
        Person.__init__(self, name_first, name_last, name_middle, address, emails, phones, birth_date)
        self.__id = advisor_id
        self.__advisor_title = advisor_title
        self.__department = department
        self.__advisees = advisees

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
    def set_advisees(self, new_advisees):
        self.__advisees = new_advisees

    def get_advisees(self):
        return self.__advisees

    # ID Setter/Getter
    def set_id(self, new_id):
        self.__id = new_id

    def get_id(self):
        return self.__id

    def __str__(self):
        return (f"Name:{self.__name_first} {self.__name_last},{self.__name_middle} "
                f"Advisor Title: {self.__advisor_title}"
                f"Department: {self.__department}"
                f"Advisee: {self.__advisees}")

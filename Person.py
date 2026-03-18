# Class to hold generic Person info
from MailingAddress import MailingAddress
from Phone import Phone
from Date import Date
from EmailAddress import EmailAddress

class Person:
    # Constructor
    def __init__(self, name_first: str, name_last: str, name_middle: str = None,
                 address: MailingAddress = None, emails: list[EmailAddress] = None, phones: list[Phone] = None, birth_date: Date = None):
        self.__name_first = name_first
        self.__name_last = name_last
        self.__name_middle = name_middle
        self.__mailing_address = address
        self.__email_addresses = emails
        self.__phones = phones
        self.__birth_date = birth_date

    # Setters
    def set_name_first(self, name_first: str):
        self.__name_first = name_first

    def set_name_last(self, name_last: str):
        self.__name_last = name_last

    def set_name_middle(self, name_middle: str):
        self.__name_middle = name_middle

    def set_mailing_address(self, address: MailingAddress):
        self.__mailing_address = address

    def set_email_addresses(self, emails: list[EmailAddress]):
        self.__email_addresses = emails

    def set_phones(self, phones: list[Phone]):
        self.__phones = phones

    def set_birth_date(self, birth_date: Date):
        self.__birth_date = birth_date

    # Getters
    def get_name_first(self):
        return self.__name_first

    def get_name_last(self):
        return self.__name_last

    def get_name_middle(self):
        return self.__name_middle

    def get_mailing_address(self):
        return self.__mailing_address

    def get_email_addresses(self):
        return self.__email_addresses

    def get_phones(self):
        return self.__phones

    def get_birth_date(self):
        return self.__birth_date

    # Overloads
    def __str__(self):
        email_str = "\n\t\t".join([
            str(email)
            for email in self.__email_addresses
        ])
        phone_str = "\n\t\t".join([
            str(phone)
            for phone in self.__phones
        ])

        return (
            f"{self.__name_last}, {self.__name_first} {self.__name_middle}: \n"
            f"DOB: {self.__birth_date}"
            f"\tAddress: {self.__mailing_address} \n"
            
            f"\tEmails: \n"
            f"\t\t{email_str} \n"
            
            f"\tPhones: \n"
            f"\t\t{phone_str} \n"
        )
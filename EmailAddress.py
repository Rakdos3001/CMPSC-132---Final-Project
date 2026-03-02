# Unites Email Information
class EmailAddress(self):
    #Constructor
    def __init__(self, email:str,email_type:str):
        self.__email = email
        self.__email_type = email_type

    #Email Setter/Getter
    def set_email(self, new_email:str):
        self.__email = new_email

    def get_email(self):
        return self.__email

    # Email Type Setter/Getter
    def set_email_type(self, new_email_type:str):
        self.__email_type = new_email_type

    def get_email(self):
        return self.__email_type

    #String Overload
    def __str__(self):
        return (f"Email: {self.__email}, Email Type: {self.__email_type}")



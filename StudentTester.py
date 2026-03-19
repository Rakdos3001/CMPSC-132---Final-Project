# Name: Joao Dias And Lex Guo
# Course: CMPSC 132
# File Name: StudentTester.py
# Date: 3/18/2026

# Short Description: Allow Students And Others To Enter, Edit, Remove, Display, Or Remove Items from List of Student Info

#Import Classes
from EmailAddress import EmailAddress
from MailingAddress import MailingAddress
from Person import Person
from Student import Student
from Date import Date
from Phone import Phone

def create_student():
    """
    Returns a new Student to be added.
    """

    # Name Information For Classes
    name_first = input("Please Enter Your First Name:")
    name_middle = input("Please Enter Your Middle Name (Type N/A if None):")
    name_last = input("Please Enter Your Last Name:")
    student_id = int(input("Please Enter Your Student ID:"))
    unified_student_info = Person(name_first, name_middle, name_last)

    # Street Info For Classes
    street_address = input("Please Enter Your Street Address:")
    city_name = input("Please Enter Your City:")
    state = input("Please Enter Your State:")
    zip_code = int(input("Please Enter Your ZIP Code:"))
    mailing_type = input("What Type of Address do you have?(Permanent,Local,etc.):")
    unified_mailing_address = MailingAddress(street_address, city_name, state, zip_code, mailing_type)

    # Email Address Info for Classes
    email_address = input("Please Enter Your Email:")
    email_type = input("What Kind Of Email is it?(Academic,Industrial,etc.):")
    unified_email = EmailAddress(email_address, email_type)

    # Phone Number Info for Classes
    phone_number = input("Please Enter Your Phone Number:")
    phone_type = input("What Kind Of Phone is it?(Cell,Home,Office):")
    unified_phone = Phone(phone_number, phone_type)

    # Birthday Info for Classes
    birth_month = int(input("Please Enter Your Birth Month:"))
    birth_day = int(input("Please Enter Your Birth Day:"))
    birth_year = int(input("Please Enter Your Birth Year:"))
    unified_birth_day = Date(birth_year, birth_month, birth_day)

    # Enrollment Info for Classes
    enrollment_date = input("Please Enter Your Enrollment Date (Month/Day/Year):")
    starting_semester = input("What Semester And Year are you starting in?:")
    major = input("What's your major?:")
    unified_extra = Student(student_id, enrollment_date, starting_semester, major)

    return unified_student_info

def main():
    #List of Student Info
    student_list = []
    while True:
        print("Hello and Welcome! Please pick an option by inputting the number assigned to it: \n")
        print(
            "1.Add A Student\n"
            "2.Edit Student Info\n"
            "3.Remove Student\n"
            "4.Display Student\n"
            "5.Exit\n"
        )
        user_input = int(input("Please Enter Your Option:"))

        if user_input == 1:
            student_list.append(create_student())
            print()

        elif user_input == 2:
            print("2")
            print()

        elif user_input == 3:
            print("3")
            print()

        elif user_input == 4:
            print("4")
            print()

        #Loop Breaks here
        elif user_input == 5:
            print("Thank you for using our program!")
            break
        else:
            print("Invalid Number. Please Try Again")


if __name__ == '__main__':
    main()

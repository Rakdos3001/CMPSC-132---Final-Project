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

    # Street Info For Classes
    street_address = input("Please Enter Your Street Address:")
    city_name = input("Please Enter Your City:")
    state = input("Please Enter Your State:")
    zip_code = int(input("Please Enter Your ZIP Code:"))
    mailing_type = input("What Type of Address do you have?(Permanent,Local,etc.):")
    unified_mailing_address = MailingAddress(street_address, city_name, state, zip_code, mailing_type)

    # Email Address Info for Classes
    email_list = []
    while True:
        email_address = input("Please Enter Your Email:")
        email_type = input("What Kind Of Email is it?(Academic,Industrial,etc.):")
        unified_email = EmailAddress(email_address, email_type)
        email_list.append(unified_email)
        ending1 = input("Do you want to enter another? (Type y/n):")
        if ending1 == "N" or "n":
            break

    # Phone Number Info for Classes
    phone_list = []
    while True:
        phone_number = input("Please Enter Your Phone Number:")
        phone_type = input("What Kind Of Phone is it?(Cell,Home,Office):")
        unified_phone = Phone(phone_number, phone_type)
        phone_list.append(unified_phone)
        ending2 = input("Do you want to enter another? (Type y/n):")
        if ending2 == "N" or "n":
            break


    # Birthday Info for Classes
    birth_month = int(input("Please Enter Your Birth Month:"))
    birth_day = int(input("Please Enter Your Birth Day:"))
    birth_year = int(input("Please Enter Your Birth Year:"))
    unified_birth_day = Date(birth_year, birth_month, birth_day)

    # Enrollment Info for Classes
    enrollment_month = int(input("Please Enter Your Enrollment Month:"))
    enrollment_day = int(input("Please Enter Your Enrollment Day:"))
    enrollment_year = int(input("Please Enter Your Enrollment Year:"))
    unified_enrollment_date = Date(enrollment_year, enrollment_month, enrollment_day)

    #Semester info for classes
    starting_semester_month = int(input("Please Enter Your Starting Semester Month:"))
    starting_semester_day = int(input("Please Enter Your Starting Semester Day:"))
    starting_semester_year = int(input("Please Enter Your Starting Semester Year:"))
    unified_starting_semester_date = Date(starting_semester_year, starting_semester_month, starting_semester_day)

    #Major info
    major = input("What's your major?:")

    unified_student_info = Student(student_id, name_first,name_last,name_middle,unified_mailing_address,
                                  email_list,phone_list,unified_birth_day,unified_enrollment_date,
                                  unified_starting_semester_date,major)

    return unified_student_info

def find_student_id(student_list: list[Student]):
    """
    Returns the index of a student in student_list, searching by student_id
    Returns -1 if index not found
    Used for editing, removing, and displaying
    """
    ids = [
        student.get_student_id()
        for student in student_list
    ]

    for (index, student_id) in enumerate(ids):
        print(f"{student_id}: {student_list[index].get_name_last()}, {student_list[index].get_name_first()}")

    target_id = int(input("Enter the id of the student: "))

    try:
        return ids.index(target_id)
    except ValueError:
        print("Student ID not found.")
        return -1

'''
def edit_info(student_list: list[Student]):
    print("This Is The Current Student Info")
    while True:
        print("")

    name_first = input("Please Enter Your First Name:")
    name_middle = input("Please Enter Your Middle Name (Type N/A if None):")
    name_last = input("Please Enter Your Last Name:")
    student_id = int(input("Please Enter Your Student ID:"))

    street_address = input("Please Enter Your Street Address:")
    city_name = input("Please Enter Your City:")
    state = input("Please Enter Your State:")
    zip_code = int(input("Please Enter Your ZIP Code:"))
    mailing_type = input("What Type of Address do you have?(Permanent,Local,etc.):")

    email_list = []
    while True:
        email_address = input("Please Enter Your Email:")
        email_type = input("What Kind Of Email is it?(Academic,Industrial,etc.):")
        unified_email = EmailAddress(email_address, email_type)
        email_list.append(unified_email)
        ending1 = input("Do you want to enter another? (Type y/n):")
        if ending1 == "N" or "n":
            break

    # Phone Number Info for Classes
    phone_list = []
    while True:
        phone_number = input("Please Enter Your Phone Number:")
        phone_type = input("What Kind Of Phone is it?(Cell,Home,Office):")
        unified_phone = Phone(phone_number, phone_type)
        phone_list.append(unified_phone)
        ending2 = input("Do you want to enter another? (Type y/n):")
        if ending2 == "N" or "n":
            break

    # Birthday Info for Classes
    birth_month = int(input("Please Enter Your Birth Month:"))
    birth_day = int(input("Please Enter Your Birth Day:"))
    birth_year = int(input("Please Enter Your Birth Year:"))
    unified_birth_day = Date(birth_year, birth_month, birth_day)

    # Enrollment Info for Classes
    enrollment_month = int(input("Please Enter Your Enrollment Month:"))
    enrollment_day = int(input("Please Enter Your Enrollment Day:"))
    enrollment_year = int(input("Please Enter Your Enrollment Year:"))
    unified_enrollment_date = Date(enrollment_year, enrollment_month, enrollment_day)

    # Semester info for classes
    starting_semester_month = int(input("Please Enter Your Starting Semester Month:"))
    starting_semester_day = int(input("Please Enter Your Starting Semester Day:"))
    starting_semester_year = int(input("Please Enter Your Starting Semester Year:"))
    unified_starting_semester_date = Date(starting_semester_year, starting_semester_month, starting_semester_day)

    # Major info
    major = input("What's your major?:")

'''
def main():
    #List of Student Info
    student_list = []
    while True:
        print("\nHello and Welcome! Please pick an option by inputting the number assigned to it: \n")
        print(
            "1.Add A Student\n"
            "2.Edit Student Info\n"
            "3.Remove Student\n"
            "4.Display Student\n"
            "5.Exit\n"
        )
        user_input = int(input("Please Enter Your Option:"))

        if user_input == 1: # Add student
            student_list.append(create_student())

        elif user_input == 2: # Edit student
            edit = edit_info(student_list)

        elif user_input == 3: # Remove student
            student_index = find_student_id(student_list)
            if student_index == -1:
                print("Student ID not found")
            else:
                confirmation = input("Are you sure you wish to delete? (Type Yes/No):")
                if confirmation == "Yes" or "yes":
                    student_list.remove(student_list[student_index])
                    print("Student Successfully Removed")

        elif user_input == 4: # Display student
            student_index = find_student_id(student_list)

            if student_index != -1:
                print(student_list[student_index])

        #Loop Breaks here
        elif user_input == 5:
            print("Thank you for using our program!")
            break
        else:
            print("Invalid Number. Please Try Again")


if __name__ == '__main__':
    main()

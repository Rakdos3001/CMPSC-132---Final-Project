# Name: Joao Dias And Lex Guo
# Course: CMPSC 132
# File Name: Tester.py
# Date: 3/18/2026

# Short Description: Allow Students And Others To Enter, Edit, Remove, Display, Or Remove Items from List of Student Info

# Import Classes
from EmailAddress import EmailAddress
from MailingAddress import MailingAddress
from Person import Person
from Student import Student
from Date import Date
from Phone import Phone

# Functions
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

    # Display students
    print("ID: NAME")
    for (index, student_id) in enumerate(ids):
        student = student_list[index]
        print(f"{student_id}: {student.get_name_last()}, {student.get_name_first()} {student.get_name_middle()}")

    # Get and validate student
    while True:
        try:
            target_id = int(input("Enter the id of the student: "))
            index = ids.index(target_id)

            return index
        except ValueError:
            print("ID not found.")
            continue

def create_student():
    """
    Creates and returns a new Student to be added.
    """

    # Name
    name_first = input("Enter first name: ")
    name_middle = input("Enter middle name: ")
    name_last = input("Enter last name: ")
    student_id = int(input("Enter student ID: "))

    # Street
    street_address = input("Enter street address: ")
    city_name = input("Enter city: ")
    state = input("Enter state: ")
    zip_code = int(input("Enter ZIP code: "))
    mailing_type = input("Enter address type (Permanent, Local, etc): ")
    unified_mailing_address = MailingAddress(street_address, city_name, state, zip_code, mailing_type)

    # Email Address
    email_list = []
    while True:
        email_address = input("Enter email address: ")
        email_type = input("Enter email type (School, Work, etc.): ")

        unified_email = EmailAddress(email_address, email_type)
        email_list.append(unified_email)

        ending1 = input("Do you want to enter another? (Type y/N): ").lower()
        if ending1 != "y":
            break

    # Phone Number
    phone_list = []
    while True:
        phone_number = input("Enter phone number: ")
        phone_type = input("Enter phone type (Cell, Home, Office): ")

        unified_phone = Phone(phone_number, phone_type)
        phone_list.append(unified_phone)

        ending2 = input("Do you want to enter another? (Type y/N): ").lower()
        if ending2 != "y":
            break

    # Birthday
    birth_month = int(input("Enter birth month: "))
    birth_day = int(input("Enter birth day: "))
    birth_year = int(input("Enter birth year: "))
    unified_birth_day = Date(birth_year, birth_month, birth_day)

    # Enrollment
    enrollment_month = int(input("Enter enrollment month: "))
    enrollment_day = int(input("Enter enrollment day: "))
    enrollment_year = int(input("Enter enrollment year: "))
    unified_enrollment_date = Date(enrollment_year, enrollment_month, enrollment_day)

    # Semester
    starting_semester_month = int(input("Enter starting semester month: "))
    starting_semester_day = int(input("Enter starting semester day: "))
    starting_semester_year = int(input("Enter starting semester year: "))
    unified_starting_semester_date = Date(starting_semester_year, starting_semester_month, starting_semester_day)

    # Major
    major = input("Enter major: ")

    # Creation
    unified_student_info = Student(student_id, name_first, name_last, name_middle, unified_mailing_address,
                                   email_list, phone_list, unified_birth_day, unified_enrollment_date,
                                   unified_starting_semester_date, major)
    print("Student Added Successfully")
    return unified_student_info

def create_example_students():
    """
    Statically creates and returns two example students for easy testing
    """

    example_student1 = Student(
        12345, "Lex", "Guo", "",
        MailingAddress("123 Street", "City 1", "State 1", 12345, "Home"),
        [
            EmailAddress("example1@psu.edu", "School"),
            EmailAddress("example1@gmail.com", "Personal")
        ],
        [
            Phone("111-222-3333", "Cell")
        ],
        Date(2006, 1, 1),
        Date(2025, 1, 1),
        Date(2026, 1, 1),
        "Computer Science"
    )
    example_student2 = Student(
        98765, "Joao", "Dias", "",
        MailingAddress("987 Street", "City 2", "State 2", 98765, "Home"),
        [
            EmailAddress("example2@psu.edu", "School"),
            EmailAddress("example2@work.com", "Work")
        ],
        [
            Phone("999-888-7777", "Home")
        ],
        Date(2007, 12, 12),
        Date(2025, 1, 1),
        Date(2026, 1, 1),
        "Computer Science"
    )

    return example_student1, example_student2

def remove_student(student_list: list[Student]):
    """
    Gets a student ID and removes that student from student_list
    """
    student_index = find_student_id(student_list)
    confirmation = input("Are you sure you wish to delete? (Type y/N): ").lower()
    if confirmation == "y":
        student_list.remove(student_list[student_index])
        print("Student Successfully Removed")

def display_student(student_list: list[Student]):
    """
    Displays the information of a student in student_list
    """
    student_index = find_student_id(student_list)
    print(student_list[student_index])

# Functions for editing
def edit_name(student: Student):
    """
    Smaller function for editing student names
    """

    while True:
        print(
            "\n"
            f"1. First Name: {student.get_name_first()}\n"
            f"2. Middle Name: {student.get_name_middle()}\n"
            f"3. Last Name: {student.get_name_last()}\n"
            f"4. Exit\n"
        )
        new_input = int(input("Enter the number of the name you'd like to change: "))
        if new_input == 1:
            new_name_first = input("Enter New First name: ")
            student.set_name_first(new_name_first)
        elif new_input == 2:
            new_name_middle = input("Enter New Middle name: ")
            student.set_name_middle(new_name_middle)
        elif new_input == 3:
            new_name_last = input("Enter New last name: ")
            student.set_name_last(new_name_last)
        elif new_input == 4:
            break

def edit_address(student: Student):
    """
    Smaller function for editing student addresses
    """

    while True:
        print(
            f"\n"
            f"1. Street Address: {student.get_mailing_address().get_street_address()}\n"
            f"2. City: {student.get_mailing_address().get_city()}\n"
            f"3. State: {student.get_mailing_address().get_state()}\n"
            f"4. Zip Code: {student.get_mailing_address().get_zip_code()}\n"
            f"5. Address Type: {student.get_mailing_address().get_address_type()}\n"
            f"6. Exit"
        )
        new_input = int(input("Enter the number of the address you'd like to change: "))
        if new_input == 1:
            new_street_address = input("Enter new street address: ")
            student.get_mailing_address().set_street_address(new_street_address)
        elif new_input == 2:
            new_city = input("Enter new city: ")
            student.get_mailing_address().set_city(new_city)
        elif new_input == 3:
            new_state = input("Enter new state: ")
            student.get_mailing_address().set_state(new_state)
        elif new_input == 4:
            new_zip = input("Enter new ZIP code: ")
            student.get_mailing_address().set_zip_code(new_zip)
        elif new_input == 5:
            new_address_type = input("Enter new address type: ")
            student.get_mailing_address().set_address_type(new_address_type)
        elif new_input == 6:
            break

def edit_emails(student: Student):
    """
    Smaller function for editing student emails
    """
    while True:
        emails = student.get_email_addresses()

        # Display emails
        print("Current Emails: ")
        for (index, phone) in enumerate(emails):
            print(f"\t{index + 1}. {phone}")

        # Menu
        print(
            f"1. Add an email \n"
            f"2. Remove an email \n"
            f"3. Exit \n"
        )
        action = int(input("Select an action: "))
        match action:
            case 1:
                email_address = input("Enter email address: ")
                email_type = input("Enter email type (School, Work, etc): ")
                emails.append(EmailAddress(email_address, email_type))
            case 2:
                # Emails are shown as index + 1, so we have to remove -1
                remove_index = int(input("Enter number of email to remove: ")) - 1
                emails.pop(remove_index)
            case 3:
                break
            case _:
                print("Invalid Action.")
                continue

def edit_phones(student: Student):
    """
    Smaller function for editing student phones
    """
    while True:
        phones = student.get_phones()

        # Display phones
        print("Current Phones: ")
        for (index, phone) in enumerate(phones):
            print(f"\t{index + 1}. {phone}")

        # Menu
        print(
            f"1. Add a phone \n"
            f"2. Remove a phone \n"
            f"3. Exit \n"
        )
        action = int(input("Select an action: "))
        match action:
            case 1:
                phone_number = input("Enter phone number: ")
                phone_type = input("Enter phone type (Cell, Home, etc): ")
                phones.append(Phone(phone_number, phone_type))
            case 2:
                # Phones are shown as index + 1, so we have to remove -1
                remove_index = int(input("Enter number of phone to remove: ")) - 1
                phones.pop(remove_index)
            case 3:
                break
            case _:
                print("Invalid Action.")
                continue

def edit_date(date: Date, date_type: str):
    """
    Smaller function for editing dates
    """
    while True:
        print(
            f"\n"
            f"1. {date_type} Month: {date.get_month()}\n"
            f"2. {date_type} Day: {date.get_day()}\n"
            f"3. {date_type} Year: {date.get_year()}\n"
            f"4. Exit"
        )
        new_input = int(input("Enter the number of the birthday info you'd like to change: "))
        if new_input == 1:
            new_month = int(input("Enter new birth month: "))
            date.set_month(new_month)
        elif new_input == 2:
            new_day = int(input("Enter new birth day: "))
            date.set_day(new_day)
        elif new_input == 3:
            new_year = int(input("Enter new birth year: "))
            date.set_year(new_year)
        elif new_input == 4:
            break

def edit_major(student: Student):
    """
    Smaller function for editing student majors
    """
    print(f"Current Major: {student.get_major()}\n")

    new_major = input("Enter new major or 1 to exit: ")
    student.set_major(new_major)

    print(f"Major changed to {new_major}")

def edit_info(student_list: list[Student]):
    """
    Allows for editing of all student info
    """
    # Gets student to update
    index = find_student_id(student_list)
    student = student_list[index]

    while True:
        email_str = "\n\t\t".join([
            str(email)
            for email in student.get_email_addresses()
        ])
        phone_str = "\n\t\t".join([
            str(phone)
            for phone in student.get_phones()
        ])

        # Lists current information that can be updated
        print(
            "This Is The Current Student Info:\n"
            # Name
            f"\t1. Name: {student.get_name_first()} {student.get_name_middle()} {student.get_name_last()} \n"
            
            # Address
            f"\t2. Address: {str(student.get_mailing_address())}\n"

            # Emails And Phones
            f"\t3. Email Addresses: \n\t\t{email_str}\n"
            f"\t4. Phone Numbers: \n\t\t{phone_str}\n"

            # Dates
            f"\t5. Birthday: {student.get_birth_date()}\n"
            f"\t6. Enrollment Date: {student.get_acceptance_date()}\n"
            f"\t7. Starting Semester: {student.get_semester_start()}\n"
                        
            f"\t8. Major: {student.get_major()}\n"
            f"\t9. Exit"
        )
        user_choice = int(input("Enter the number of the info you'd like to change: "))

        # Choices for user to update
        # Adds loops so user can do it repeatedly without leaving
        if user_choice == 1:
            edit_name(student)

        elif user_choice == 2:
            edit_address(student)

        # Email and Phone
        elif user_choice == 3: # Email
            edit_emails(student)

        elif user_choice == 4: # Phone
            edit_phones(student)

        # Dates
        elif user_choice == 5: # Date of birth
            edit_date(student.get_birth_date(), "Birth")

        elif user_choice == 6: # Enrollment date
            edit_date(student.get_acceptance_date(), "Enrollment")

        elif user_choice == 7: # Start of semester
            edit_date(student.get_semester_start(), "Semester Start")

        # Major
        elif user_choice == 8:
            edit_major(student)

        # End
        elif user_choice == 9:
            break
        else:
            print("Invalid action.")
            continue

        print("Changes successfully made.")

# Main and running
def main():
    # List of Student Info
    student_list = []
    s1, s2 = create_example_students()
    student_list.append(s1)
    student_list.append(s2)
    while True:
        print("\nHello and Welcome! Please pick an option by inputting the number assigned to it: \n")
        print(
            "1. Add A Student\n"
            "2. Edit Student Info\n"
            "3. Remove Student\n"
            "4. Display Student\n"
            "5. Exit\n"
        )
        user_input = int(input("Enter Option: "))

        if user_input == 1:  # Add student
            student_list.append(create_student())

        elif user_input == 2:  # Edit student
            edit_info(student_list)

        elif user_input == 3:  # Remove student
            remove_student(student_list)

        elif user_input == 4:  # Display student
            display_student(student_list)

        # Loop Breaks here
        elif user_input == 5:
            print("Thank you for using our program!")
            break
        else:
            print("Invalid Number. Please Try Again")


if __name__ == '__main__':
    main()
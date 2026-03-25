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
    name_first = input("Enter first name: ")
    name_middle = input("Enter middle name (Type N/A if None): ")
    name_last = input("Enter last name: ")
    student_id = int(input("Enter student ID: "))

    # Street Info For Classes
    street_address = input("Enter street address: ")
    city_name = input("Enter city: ")
    state = input("Enter state: ")
    zip_code = int(input("Enter ZIP code: "))
    mailing_type = input("Enter address type (Permanent, Local, etc): ")
    unified_mailing_address = MailingAddress(street_address, city_name, state, zip_code, mailing_type)

    # Email Address Info for Classes
    email_list = []
    while True:
        email_address = input("Enter email address: ")
        email_type = input("Enter email type (School, Work, etc.): ")

        unified_email = EmailAddress(email_address, email_type)
        email_list.append(unified_email)

        ending1 = input("Do you want to enter another? (Type Y/n): ").lower()
        if ending1 != "y":
            break

    # Phone Number Info for Classes
    phone_list = []
    while True:
        phone_number = input("Enter phone number: ")
        phone_type = input("Enter phone type (Cell, Home, Office): ")

        unified_phone = Phone(phone_number, phone_type)
        phone_list.append(unified_phone)

        ending2 = input("Do you want to enter another? (Type Y/n): ").lower()
        if ending2 != "y":
            break


    # birthday Info for Classes
    birth_month = int(input("Enter birth month: "))
    birth_day = int(input("Enter birth day: "))
    birth_year = int(input("Enter birth year: "))
    unified_birth_day = Date(birth_year, birth_month, birth_day)

    # Enrollment Info for Classes
    enrollment_month = int(input("Enter enrollment month: "))
    enrollment_day = int(input("Enter enrollment day: "))
    enrollment_year = int(input("Enter enrollment year: "))
    unified_enrollment_date = Date(enrollment_year, enrollment_month, enrollment_day)

    #Semester info for classes
    starting_semester_month = int(input("Enter starting semester month: "))
    starting_semester_day = int(input("Enter starting Semester day: "))
    starting_semester_year = int(input("Enter starting Semester year: "))
    unified_starting_semester_date = Date(starting_semester_year, starting_semester_month, starting_semester_day)

    #Major info
    major = input("Enter major: ")

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
    index = ids.index(target_id)

    while index == -1:
        target_id = int(input("ID not found. Enter the id of the student: "))
        index = ids.index(target_id)

    return index

#Edit Info
def edit_info(student_list: list[Student]):
    index = find_student_id(student_list)

    student = student_list[index]
    print("This Is The Current Student Info")
    while True:
        print(
            # Names
            f"1. First Name: {student.get_name_first()}\n"
            f"2. Middle Name: {student.get_name_last()}\n"
            f"3. Last Name: {student.get_name_middle()}\n"
            
            # Address
            f"4. Street Address: {student.get_mailing_address().get_street_address()}\n"
            f"5. City Name: {student.get_mailing_address().get_city()}\n"
            f"6. State: {student.get_mailing_address().get_state()}\n"
            f"7. Zip Code: {student.get_mailing_address().get_zip_code()}\n"
            f"8. Mail Type: {student.get_mailing_address().get_address_type()}\n"
            
            # Emails And Phones
            f'''
            f"9. Email Addresses: {student.get_email_addresses()}\n"
            f"10. Phone Numbers: {student.get_phones()}\n"
            '''
            
            # Misc
            f"11. Birth Month: {student.get_birth_date().get_month()}\n"
            f"12. Birth Day: {student.get_birth_date().get_day()}\n"
            f"13. Birth Year: {student.get_birth_date().get_year()}\n"
            
            f"14. Enrollment Month: {student.get_acceptance_date().get_month()}\n"
            f"15. Enrollment Day: {student.get_acceptance_date().get_day()}\n"
            f"16. Enrollment Year: {student.get_acceptance_date().get_year()}\n"
            
            f"17. Starting Semester Month: {student.get_semester_start().get_month()}\n"
            f"18. Starting Semester Day: {student.get_semester_start().get_day()}\n"
            f"19. Starting Semester Year: {student.get_semester_start().get_year()}\n"
            f"20. Major: {student.get_major()}\n"
            
            f"21. Exit"
        )
        user_choice = int(input("Enter the number of the info you'd like to change: "))

        #Names
        if user_choice == 1:
            new_input1 = input("Enter new first name: ")
            student.set_name_first(new_input1)
        elif user_choice == 2:
            new_input2 = input("Enter new last name: ")
            student.set_name_last(new_input2)
        elif user_choice == 3:
            new_input3 = input("Enter new middle name: ")
            student.set_name_middle(new_input3)

        # Mailing Address
        elif user_choice == 4:
            new_input4 = input("Enter new street address: ")
            student.get_mailing_address().set_street_address(new_input4)
        elif user_choice == 5:
            new_input5 = input("Enter new city: ")
            student.get_mailing_address().set_city(new_input5)
        elif user_choice == 6:
            new_input6 = input("Enter new state: ")
            student.get_mailing_address().set_state(new_input6)
        elif user_choice == 7:
            new_input7 = input("Enter new zip Code: ")
            student.get_mailing_address().set_zip_code(new_input7)
        elif user_choice == 8:
            new_input8 = input("Enter new address type: ")
            student.get_mailing_address().set_address_type(new_input8)

        # Email and Phone
        elif user_choice == 9:
            emails = student.get_email_addresses()

            # Display emails
            print("Current Emails: ")
            for (index, phone) in enumerate(emails):
                print(f"\t{index + 1}. {phone}")

            # Menu
            print(
                f"1. Add an email \n"
                f"2. Remove an email \n"
                f"3. Go back \n"
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
                case _:
                    print("Invalid Action.")
                    continue

        elif user_choice == 10:
            phones = student.get_phones()

            # Display phones
            print("Current Phones: ")
            for (index, phone) in enumerate(phones):
                print(f"\t{index + 1}. {phone}")

            # Menu
            print(
                f"1. Add a phone \n"
                f"2. Remove a phone \n"
                f"3. Go back \n"
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
                case _:
                    print("Invalid Action.")
                    continue

        # Misc
        elif user_choice == 11:
            new_input13 = input("Enter new birth month: ")
            student.get_birth_date().set_month(new_input13)
        elif user_choice == 12:
            new_input14 = input("Enter new birth day: ")
            student.get_birth_date().set_day(new_input14)
        elif user_choice == 13:
            new_input15 = input("Enter new birth year: ")
            student.get_birth_date().set_year(new_input15)

        elif user_choice == 14:
            new_input16 = input("Enter new enrollment month: ")
            student.get_acceptance_date().set_month(new_input16)
        elif user_choice == 15:
            new_input17 = input("Enter new enrollment day: ")
            student.get_acceptance_date().set_day(new_input17)
        elif user_choice == 16:
            new_input18 = input("Enter new enrollment year: ")
            student.get_acceptance_date().set_year(new_input18)

        elif user_choice == 17:
            new_input19 = input("Enter new starting semester month: ")
            student.get_semester_start().set_month(new_input19)
        elif user_choice == 18:
            new_input20 = input("Enter new starting semester day: ")
            student.get_semester_start().set_month(new_input20)
        elif user_choice == 19:
            new_input21 = input("Enter new starting semester year: ")
            student.get_semester_start().set_month(new_input21)
        elif user_choice == 20:
            new_input22 = input("Enter new Major: ")
            student.set_major(new_input22)

        elif user_choice == 21:
            break
        else:
            print("Invalid action.")
            continue


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
        user_input = int(input("Enter Option: "))

        if user_input == 1: # Add student
            student_list.append(create_student())

        elif user_input == 2: # Edit student
            edit_info(student_list)

        elif user_input == 3: # Remove student
            student_index = find_student_id(student_list)
            confirmation = input("Are you sure you wish to delete? (Type Yes/No): ").lower()
            if confirmation == "yes":
                student_list.remove(student_list[student_index])
                print("Student Successfully Removed")

        elif user_input == 4: # Display student
            student_index = find_student_id(student_list)
            print(student_list[student_index])

        #Loop Breaks here
        elif user_input == 5:
            print("Thank you for using our program!")
            break
        else:
            print("Invalid Number. Please Try Again")


if __name__ == '__main__':
    main()

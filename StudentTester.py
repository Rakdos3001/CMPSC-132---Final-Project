# Name: Joao Dias And Lex Guo
# Course: CMPSC 132
# File Name: StudentTester.py
# Date: 3/18/2026

# Short Description: Allow Students And Others To Enter, Edit, Remove, Display, Or Remove Items from List of Student Info

# Import Classes
from EmailAddress import EmailAddress
from MailingAddress import MailingAddress
from Person import Person
from Student import Student
from Date import Date
from Phone import Phone

#Displays list of students and then asks user to enter id to show
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

#Function to create student information. Includes sending to other classes
def create_student():
    """
    Returns a new Student to be added.
    """

    # Name
    name_first = input("Enter first name: ")
    name_middle = input("Enter middle name (Type N/A if None): ")
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

        ending1 = input("Do you want to enter another? (Type Y/n): ").lower()
        if ending1 != "y":
            break

    # Phone Number
    phone_list = []
    while True:
        phone_number = input("Enter phone number: ")
        phone_type = input("Enter phone type (Cell, Home, Office): ")

        unified_phone = Phone(phone_number, phone_type)
        phone_list.append(unified_phone)

        ending2 = input("Do you want to enter another? (Type Y/n): ").lower()
        if ending2 != "y":
            break

    # Birthday
    birth_month = int(input("Enter birth month (Just Numbers, No Words): "))
    birth_day = int(input("Enter birth day: "))
    birth_year = int(input("Enter birth year: "))
    unified_birth_day = Date(birth_year, birth_month, birth_day)

    # Enrollment
    enrollment_month = int(input("Enter enrollment month (Just Numbers, No Words): "))
    enrollment_day = int(input("Enter enrollment day: "))
    enrollment_year = int(input("Enter enrollment year: "))
    unified_enrollment_date = Date(enrollment_year, enrollment_month, enrollment_day)

    # Semester
    starting_semester_month = int(input("Enter starting semester month (Just Numbers, No Words): "))
    starting_semester_day = int(input("Enter starting semester day: "))
    starting_semester_year = int(input("Enter starting semester year: "))
    unified_starting_semester_date = Date(starting_semester_year, starting_semester_month, starting_semester_day)

    # Major
    major = input("Enter major: ")

    # Creation
    unified_student_info = Student(student_id, name_first, name_last, name_middle, unified_mailing_address,
                                   email_list, phone_list, unified_birth_day, unified_enrollment_date,
                                   unified_starting_semester_date, major)

    return unified_student_info

#Function in order to edit info
def edit_info(student_list: list[Student]):
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

#List of current info to be updated
        print(
            "This Is The Current Student Info\n"

            # Names
            f"\t1. First Name: {student.get_name_first()}\n"
            f"\t2. Middle Name: {student.get_name_last()}\n"
            f"\t3. Last Name: {student.get_name_middle()}\n"

            # Address
            f"\t4. Street Address: {student.get_mailing_address().get_street_address()}\n"
            f"\t5. City Name: {student.get_mailing_address().get_city()}\n"
            f"\t6. State: {student.get_mailing_address().get_state()}\n"
            f"\t7. Zip Code: {student.get_mailing_address().get_zip_code()}\n"
            f"\t8. Mail Type: {student.get_mailing_address().get_address_type()}\n"

            # Emails And Phones
            f"\t9. Email Addresses: \n\t{email_str}\n"
            f"\t10. Phone Numbers: \n\t{phone_str}\n"

            # Misc
            f"\t11. Birth Month: {student.get_birth_date().get_month()}\n"
            f"\t12. Birth Day: {student.get_birth_date().get_day()}\n"
            f"\t13. Birth Year: {student.get_birth_date().get_year()}\n"

            f"\t14. Enrollment Month: {student.get_acceptance_date().get_month()}\n"
            f"\t15. Enrollment Day: {student.get_acceptance_date().get_day()}\n"
            f"\t16. Enrollment Year: {student.get_acceptance_date().get_year()}\n"

            f"\t17. Starting Semester Month: {student.get_semester_start().get_month()}\n"
            f"\t18. Starting Semester Day: {student.get_semester_start().get_day()}\n"
            f"\t19. Starting Semester Year: {student.get_semester_start().get_year()}\n"
            f"\t20. Major: {student.get_major()}\n"

            f"\t21. Exit"
        )
        user_choice = int(input("Enter the number of the info you'd like to change: "))

        # Choices for user to update
        if user_choice == 1:
            new_name_first = input("Enter new first name: ")
            student.set_name_first(new_name_first)
        elif user_choice == 2:
            new_name_last = input("Enter new last name: ")
            student.set_name_last(new_name_last)
        elif user_choice == 3:
            new_name_mid = input("Enter new middle name: ")
            student.set_name_middle(new_name_mid)

        # Mailing Address
        elif user_choice == 4:
            new_street_address = input("Enter new street address: ")
            student.get_mailing_address().set_street_address(new_street_address)
        elif user_choice == 5:
            new_city = input("Enter new city: ")
            student.get_mailing_address().set_city(new_city)
        elif user_choice == 6:
            new_state = input("Enter new state: ")
            student.get_mailing_address().set_state(new_state)
        elif user_choice == 7:
            new_zip = input("Enter new ZIP code: ")
            student.get_mailing_address().set_zip_code(new_zip)
        elif user_choice == 8:
            new_address_type = input("Enter new address type: ")
            student.get_mailing_address().set_address_type(new_address_type)

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

        # Misc choices for user to update
        elif user_choice == 11:
            new_birth_month = input("Enter new birth month: ")
            student.get_birth_date().set_month(new_birth_month)
        elif user_choice == 12:
            new_birth_day = input("Enter new birth day: ")
            student.get_birth_date().set_day(new_birth_day)
        elif user_choice == 13:
            new_birth_year = input("Enter new birth year: ")
            student.get_birth_date().set_year(new_birth_year)

        elif user_choice == 14:
            new_enroll_month = input("Enter new enrollment month: ")
            student.get_acceptance_date().set_month(new_enroll_month)
        elif user_choice == 15:
            new_enroll_day = input("Enter new enrollment day: ")
            student.get_acceptance_date().set_day(new_enroll_day)
        elif user_choice == 16:
            new_enroll_year = input("Enter new enrollment year: ")
            student.get_acceptance_date().set_year(new_enroll_year)

        elif user_choice == 17:
            new_semester_month = input("Enter new starting semester month: ")
            student.get_semester_start().set_month(new_semester_month)
        elif user_choice == 18:
            new_semester_day = input("Enter new starting semester day: ")
            student.get_semester_start().set_month(new_semester_day)
        elif user_choice == 19:
            new_semester_year = input("Enter new starting semester year: ")
            student.get_semester_start().set_month(new_semester_year)
        elif user_choice == 20:
            new_major = input("Enter new major: ")
            student.set_major(new_major)

        elif user_choice == 21:
            break
        else:
            print("Invalid action.")
            continue

#Removes student based on id entered
def remove_student(student_list: list[Student]):
    student_index = find_student_id(student_list)
    confirmation = input("Are you sure you wish to delete? (Type Yes/No): ").lower()
    if confirmation == "yes":
        student_list.remove(student_list[student_index])
        print("Student Successfully Removed")

#Displays info based on student id
def display_student(student_list: list[Student]):
    student_index = find_student_id(student_list)
    print(student_list[student_index])


def main():
    # List of Student Info
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

'''
/usr/local/bin/python3.13 /Users/joaodias/Desktop/CMPSC-132---Final-Project/Paste/StudentTester.py 

Hello and Welcome! Please pick an option by inputting the number assigned to it: 

1.Add A Student
2.Edit Student Info
3.Remove Student
4.Display Student
5.Exit

Enter Option: 1
Enter first name: Joao
Enter middle name (Type N/A if None): Pedro
Enter last name: Dias
Enter student ID: 12345
Enter street address: 804 Shadebrush Ridge
Enter city: West Chester
Enter state: PA
Enter ZIP code: 19382
Enter address type (Permanent, Local, etc): Local
Enter email address: EmailExample@100
Enter email type (School, Work, etc.): School
Do you want to enter another? (Type Y/n): y
Enter email address: EmailExample@200
Enter email type (School, Work, etc.): Work
Do you want to enter another? (Type Y/n): n
Enter phone number: 646-644-7777
Enter phone type (Cell, Home, Office): Cell
Do you want to enter another? (Type Y/n): y
Enter phone number: 999-999-9999
Enter phone type (Cell, Home, Office): Home
Do you want to enter another? (Type Y/n): n
Enter birth month (Just Numbers, No Words): 9
Enter birth day: 19
Enter birth year: 2000
Enter enrollment month (Just Numbers, No Words): 8
Enter enrollment day: 19
Enter enrollment year: 2021
Enter starting semester month (Just Numbers, No Words): 11
Enter starting semester day: 11
Enter starting semester year: 2022
Enter major: History

Hello and Welcome! Please pick an option by inputting the number assigned to it: 

1.Add A Student
2.Edit Student Info
3.Remove Student
4.Display Student
5.Exit

Enter Option: 4
12345: Dias, Joao Pedro
Enter the id of the student: 12345
Dias, Joao Pedro: 
	DOB: 9/19/2000
	Address: 804 Shadebrush Ridge, West Chester, PA 19382 (Local) 
	Emails: 
		EmailExample@100 (School)
		EmailExample@200 (Work) 
	Phones: 
		646-644-7777 (Cell)
		999-999-9999 (Home) 

	Student ID: 12345
	Acceptance Date: 8/19/2021
	Semester Starts: 11/11/2022
	Major: History


Hello and Welcome! Please pick an option by inputting the number assigned to it: 

1.Add A Student
2.Edit Student Info
3.Remove Student
4.Display Student
5.Exit

Enter Option: 2
12345: Dias, Joao Pedro
Enter the id of the student: 12345
This Is The Current Student Info
	1. First Name: Joao
	2. Middle Name: Dias
	3. Last Name: Pedro
	4. Street Address: 804 Shadebrush Ridge
	5. City Name: West Chester
	6. State: PA
	7. Zip Code: 19382
	8. Mail Type: Local
	9. Email Addresses: 
	EmailExample@100 (School)
		EmailExample@200 (Work)
	10. Phone Numbers: 
	646-644-7777 (Cell)
		999-999-9999 (Home)
	11. Birth Month: 9
	12. Birth Day: 19
	13. Birth Year: 2000
	14. Enrollment Month: 8
	15. Enrollment Day: 19
	16. Enrollment Year: 2021
	17. Starting Semester Month: 11
	18. Starting Semester Day: 11
	19. Starting Semester Year: 2022
	20. Major: History
	21. Exit
Enter the number of the info you'd like to change: 11
Enter new birth month: 3
This Is The Current Student Info
	1. First Name: Joao
	2. Middle Name: Dias
	3. Last Name: Pedro
	4. Street Address: 804 Shadebrush Ridge
	5. City Name: West Chester
	6. State: PA
	7. Zip Code: 19382
	8. Mail Type: Local
	9. Email Addresses: 
	EmailExample@100 (School)
		EmailExample@200 (Work)
	10. Phone Numbers: 
	646-644-7777 (Cell)
		999-999-9999 (Home)
	11. Birth Month: 3
	12. Birth Day: 19
	13. Birth Year: 2000
	14. Enrollment Month: 8
	15. Enrollment Day: 19
	16. Enrollment Year: 2021
	17. Starting Semester Month: 11
	18. Starting Semester Day: 11
	19. Starting Semester Year: 2022
	20. Major: History
	21. Exit
Enter the number of the info you'd like to change: 21

Hello and Welcome! Please pick an option by inputting the number assigned to it: 

1.Add A Student
2.Edit Student Info
3.Remove Student
4.Display Student
5.Exit

Enter Option: 3
12345: Dias, Joao Pedro
Enter the id of the student: 12345
Are you sure you wish to delete? (Type Yes/No): yes
Student Successfully Removed

Hello and Welcome! Please pick an option by inputting the number assigned to it: 

1.Add A Student
2.Edit Student Info
3.Remove Student
4.Display Student
5.Exit

Enter Option: 5
Thank you for using our program!

Process finished with exit code 0
'''
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
    print("Student Added Successfully")
    return unified_student_info


def example_students():
    unified_birth_day_example = Date(2006, 12, 11)
    unified_enrollment_date_example = Date(2010, 1, 15)
    unified_starting_semester_date_example = Date(2020, 11, 9)
    unified_mailing_address_example = MailingAddress("804 Bird Road", "Media", "PA", 19191, "Local")

    email_list_example = []
    unified_email = EmailAddress("ExampleEmail@100", "Personal")
    email_list_example.append(unified_email)

    phone_list_example = []
    unified_phone = Phone("215-191-5222", "Personal")
    phone_list_example.append(unified_phone)

    example_student1 = Student(12345,"Gina","Wu","Chen",unified_mailing_address_example,
                                   email_list_example, phone_list_example, unified_birth_day_example, unified_enrollment_date_example,
                                   unified_starting_semester_date_example, "Art")
    example_student2 = Student(98765,"Ken","Khan","Katsuragi",unified_mailing_address_example,
                                   email_list_example, phone_list_example, unified_birth_day_example, unified_enrollment_date_example,
                                   unified_starting_semester_date_example, "History")

    return example_student1,example_student2


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
            "This Is The Current Student Info\n")
            # Name
        print(
            f"1. Name: {student.get_name_first()} {student.get_name_middle()},{student.get_name_last()} \n"
            
            #Address
            f"2. Address: {student.get_mailing_address().get_street_address()}, {student.get_mailing_address().get_city()}, {student.get_mailing_address().get_state()} {student.get_mailing_address().get_zip_code()} ({student.get_mailing_address().get_address_type()})\n"
           
            # Emails And Phones
            f"\t3. Email Addresses: \n\t{email_str}\n"
            
            f"\t4. Phone Numbers: \n\t{phone_str}\n"
            

            #Dates
            f"5. Birthday:{student.get_birth_date().get_month()}/{student.get_birth_date().get_day()}/{student.get_birth_date().get_year()}\n"
            
            f"6. Enrollment Date: {student.get_acceptance_date().get_month()}/{student.get_acceptance_date().get_day()}/{student.get_acceptance_date().get_year()}\n"
            
            f"7. Starting Semester: {student.get_semester_start().get_month()}/{student.get_semester_start().get_day()}/{student.get_semester_start().get_year()}\n"
            
            f"8. Major: {student.get_major()}\n"
            
            f"9. Exit"
        )
        user_choice = int(input("Enter the number of the info you'd like to change: "))

        # Choices for user to update
        #Adds loops so user can do it repeadetly without leaving
        if user_choice == 1:
            while True:
                print()
                print(f"1. First Name: {student.get_name_first()}\n"
                      f"2. Middle Name: {student.get_name_middle()}\n"
                      f"3. Last Name: {student.get_name_last()}\n"
                      f"4. Exit\n")
                new_input = int(input("Enter the number of the name you'd like to change: "))
                if new_input == 1:
                    new_name_first = input("Enter New First name: ")
                    student.set_name_first(new_name_first)
                elif new_input == 2:
                    new_name_middle = input("Enter New Middle name: ")
                    student.set_name_middle(new_name_middle)
                elif new_input == 3:
                    new_name_first = input("Enter New last name: ")
                    student.set_name_last(new_name_last)
                elif new_input == 4:
                    break


        elif user_choice == 2:
            while True:
                print()
                print(f"1. Street Address: {student.get_mailing_address().get_street_address()}\n"
                      f"2. City: {student.get_mailing_address().get_city()}\n"
                      f"3. State: {student.get_mailing_address().get_state()}\n"
                      f"4. Zip Code: {student.get_mailing_address().get_zip_code()}\n"
                      f"5. Address Type: {student.get_mailing_address().get_address_type()}\n"
                      f"6. Exit")
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


        # Email and Phone
        elif user_choice == 3:
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

        elif user_choice == 4:
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

        # Misc choices for user to update
        elif user_choice == 5:
            while True:
                print()
                print(f"1. Birthday Month: {student.get_birth_date().get_month()}\n"
                      f"2. Birthday Day: {student.get_birth_date().get_day()}\n"
                      f"3. Birthday Year: {student.get_birth_date().get_year()}\n"
                      f"4. Exit")
                new_input = int(input("Enter the number of the birthday info you'd like to change: "))
                if new_input == 1:
                    new_birth_month = input("Enter new birth month: ")
                    student.get_birth_date().set_month(new_birth_month)
                elif new_input == 2:
                    new_birth_day = input("Enter new birth day: ")
                    student.get_birth_date().set_day(new_birth_day)
                elif new_input == 3:
                    new_birth_year = input("Enter new birth year: ")
                    student.get_birth_date().set_year(new_birth_year)
                elif new_input == 4:
                    break


        elif user_choice == 6:
            while True:
                print()
                print(f"1. Enrollment Month: {student.get_acceptance_date().get_month()}\n"
                      f"2. Enrollment Day: {student.get_acceptance_date().get_day()}\n"
                      f"3. Enrollment Year: {student.get_acceptance_date().get_year()}\n"
                      f"4. Exit")
                new_input = int(input("Enter the number of enrollment info you'd like to change: "))
                if new_input == 1:
                    new_enroll_month = input("Enter new enrollment month: ")
                    student.get_acceptance_date().set_month(new_enroll_month)
                elif new_input == 2:
                    new_enroll_day = input("Enter new enrollment day: ")
                    student.get_acceptance_date().set_day(new_enroll_day)
                elif new_input == 3:
                    new_enroll_year = input("Enter new enrollment year: ")
                    student.get_acceptance_date().set_year(new_enroll_year)
                elif new_input == 4:
                    break

        elif user_choice == 7:
            while True:
                print()
                print(f"1. Starting Semester Month: {student.get_semester_start().get_month()}\n"
                      f"2. Starting Semester Day: {student.get_semester_start().get_day()}\n"
                      f"3. Starting Semester Year: {student.get_semester_start().get_year()}\n"
                      f"4. Exit")
                new_input = int(input("Enter the number of semester info you'd like to change: "))
                if new_input == 1:
                    new_semester_month = input("Enter new starting semester month: ")
                    student.get_semester_start().set_month(new_semester_month)
                elif new_input == 2:
                    new_semester_day = input("Enter new starting semester day: ")
                    student.get_semester_start().set_month(new_semester_day)
                elif new_input == 3:
                    new_semester_year = input("Enter new starting semester year: ")
                    student.get_semester_start().set_month(new_semester_year)
                elif new_input == 4:
                    break

        elif user_choice == 8:
            while True:
                print(f"Major: {student.get_major()}\n")
                new_major = input("Enter new major or 1 to exit: ")
                if new_major == "1":
                    break
                else:
                    student.set_major(new_major)

        elif user_choice == 9:
          print("Edits Successfully Implemented")
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
    s1, s2 = example_students()
    student_list.append(s1)
    student_list.append(s2)
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

Enter Option: 4
12345: Wu, Gina Chen
98765: Khan, Ken Katsuragi
Enter the id of the student: 12345
Wu, Gina Chen: 
	DOB: 12/11/2006
	Address: 804 Bird Road, Media, PA 19191 (Local) 
	Emails: 
		ExampleEmail@100 (Personal) 
	Phones: 
		215-191-5222 (Personal) 

	Student ID: 12345
	Acceptance Date: 1/15/2010
	Semester Starts: 11/9/2020
	Major: Art


Hello and Welcome! Please pick an option by inputting the number assigned to it: 

1.Add A Student
2.Edit Student Info
3.Remove Student
4.Display Student
5.Exit

Enter Option: 3
12345: Wu, Gina Chen
98765: Khan, Ken Katsuragi
Enter the id of the student: 98765
Are you sure you wish to delete? (Type Yes/No): yes
Student Successfully Removed

Hello and Welcome! Please pick an option by inputting the number assigned to it: 

1.Add A Student
2.Edit Student Info
3.Remove Student
4.Display Student
5.Exit

Enter Option: 2
12345: Wu, Gina Chen
Enter the id of the student: 12345
This Is The Current Student Info

1. Name: Gina Chen,Wu 
2. Address: 804 Bird Road, Media, PA 19191 (Local)
	3. Email Addresses: 
	ExampleEmail@100 (Personal)
	4. Phone Numbers: 
	215-191-5222 (Personal)
5. Birthday:12/11/2006
6. Enrollment Date: 1/15/2010
7. Starting Semester: 11/9/2020
8. Major: Art
9. Exit
Enter the number of the info you'd like to change: 1

1. First Name: Gina
2. Middle Name: Chen
3. Last Name: Wu
4. Exit

Enter the number of the name you'd like to change: 2
Enter New Middle name: Chun

1. First Name: Gina
2. Middle Name: Chun
3. Last Name: Wu
4. Exit

Enter the number of the name you'd like to change: 4
This Is The Current Student Info

1. Name: Chun Chen,Wu 
2. Address: 804 Bird Road, Media, PA 19191 (Local)
	3. Email Addresses: 
	ExampleEmail@100 (Personal)
	4. Phone Numbers: 
	215-191-5222 (Personal)
5. Birthday:12/11/2006
6. Enrollment Date: 1/15/2010
7. Starting Semester: 11/9/2020
8. Major: Art
9. Exit
Enter the number of the info you'd like to change: 8
Major: Art

1. Exit
Enter new major or 1 to exit: History
Major: History

1. Exit
Enter new major or 1 to exit: 1
This Is The Current Student Info

1. Name: Chun Chen,Wu 
2. Address: 804 Bird Road, Media, PA 19191 (Local)
	3. Email Addresses: 
	ExampleEmail@100 (Personal)
	4. Phone Numbers: 
	215-191-5222 (Personal)
5. Birthday:12/11/2006
6. Enrollment Date: 1/15/2010
7. Starting Semester: 11/9/2020
8. Major: History
9. Exit
Enter the number of the info you'd like to change: 9
Edits Successfully Implemented

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
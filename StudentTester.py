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
        email_type = input("What Kind Of Email is it? (Academic,Industrial,etc.):")
        unified_email = EmailAddress(email_address, email_type)
        email_list.append(unified_email)
        ending1 = input("Do you want to enter another? (Type y/n):")
        if ending1 == "n":
            break

    # Phone Number Info for Classes
    phone_list = []
    while True:
        phone_number = input("Please Enter Your Phone Number:")
        phone_type = input("What Kind Of Phone is it? (Cell,Home,Office):")
        unified_phone = Phone(phone_number, phone_type)
        phone_list.append(unified_phone)
        ending2 = input("Do you want to enter another? (Type y/n):")
        if ending2 == "n":
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

#Edit Info
def edit_info(student_list: list[Student]):
    index = find_student_id(student_list)
    if index == -1:
        return

    student = student_list[index]
    print("This Is The Current Student Info")
    while True:
        print(
        f"1. First Name: {student.get_name_first()}\n"
        f"2. Middle Name: {student.get_name_last()}\n"
        f"3. Last Name: {student.get_name_middle()}\n"
        
        f"4. Street Address: {student.get_mailing_address().get_street_address()}\n"
        f"5. City Name: {student.get_mailing_address().get_city()}\n"
        f"6. State: {student.get_mailing_address().get_state()}\n"
        f"7. Zip Code: {student.get_mailing_address().get_zip_code()}\n"
        f"8. Mail Type: {student.get_mailing_address().get_address_type()}\n"
    #Email And Phone Here
        '''
        f"9. Email Address: {}\n"
        f"10. Email Type: {}\n"
        f"11. Phone Number: {}\n"
        f"12. Phone Type: {}\n"
        '''
    #Rest
        f"13. Birth Month: {student.get_birth_date().get_month()}\n"
        f"14. Birth Day: {student.get_birth_date().get_day()}\n"
        f"15. Birth Year: {student.get_birth_date().get_year()}\n"
        
        f"16. Enrollment Month: {student.get_acceptance_date().get_month()}\n"
        f"17. Enrollment Day: {student.get_acceptance_date().get_day()}\n"
        f"18. Enrollment Year: {student.get_acceptance_date().get_year()}\n"
        
        f"19. Starting Semester Month: {student.get_semester_start().get_month()}\n"
        f"20. Starting Semester Day: {student.get_semester_start().get_day()}\n"
        f"21. Starting Semester Year: {student.get_semester_start().get_year()}\n"
        f"22. Major: {student.get_major()}\n"
        )
        print()
        User_Choice = int(input("Please Enter The Number of the info you'd like to change:"))
        #Names
        if User_Choice == 1:
            new_input1 = input("Please Enter A New First Name:")
            student.set_name_first(new_input1)
        elif User_Choice == 2:
            new_input2 = input("Please Enter A New Last Name:")
            student.set_name_last(new_input2)
        elif User_Choice == 3:
            new_input3 = input("Please Enter A New Middle Name:")
            student.set_name_middle(new_input3)

        #Mailing Address
        elif User_Choice == 4:
            new_input4 = input("Please Enter A New Street Address:")
            student.get_mailing_address().set_street_address(new_input4)
        elif User_Choice == 5:
            new_input5 = input("Please Enter A New City:")
            student.get_mailing_address().set_city(new_input5)
        elif User_Choice == 6:
            new_input6 = input("Please Enter A New State:")
            student.get_mailing_address().set_state(new_input6)
        elif User_Choice == 7:
            new_input7 = input("Please Enter A New Zip Code:")
            student.get_mailing_address().set_zip_code(new_input7)
        elif User_Choice == 8:
            new_input8 = input("Please Enter A New Address Type:")
            student.get_mailing_address().set_address_type(new_input8)
            '''
            #Choices corresponding with email and phone 
        elif User_Choice == 9:
        elif User_Choice == 10:
        elif User_Choice == 11:
        elif User_Choice == 12:
        '''
        elif User_Choice == 13:
            new_input13 = input("Please Enter A New Birth Month:")
            student.get_birth_date().set_month(new_input13)
        elif User_Choice == 14:
            new_input14 = input("Please Enter A New Birth Day:")
            student.get_birth_date().set_day(new_input14)
        elif User_Choice == 15:
            new_input15 = input("Please Enter A New Birth Year:")
            student.get_birth_date().set_year(new_input15)

        elif User_Choice == 16:
            new_input16 = input("Please Enter A New Enrollment Month:")
            student.get_acceptance_date().set_month(new_input16)
        elif User_Choice == 17:
            new_input17 = input("Please Enter A New Enrollment Day:")
            student.get_acceptance_date().set_day(new_input17)
        elif User_Choice == 18:
            new_input18 = input("Please Enter A New Enrollment Year:")
            student.get_acceptance_date().set_year(new_input18)

        elif User_Choice == 19:
            new_input19 = input("Please Enter A New Starting Semester Month:")
            student.get_semester_start().set_month(new_input19)
        elif User_Choice == 20:
            new_input20 = input("Please Enter A New Starting Semester Day:")
            student.get_semester_start().set_month(new_input20)
        elif User_Choice == 21:
            new_input21 = input("Please Enter A New Starting Semester Year:")
            student.get_semester_start().set_month(new_input21)
        elif User_Choice == 22:
            new_input22 = input("Please Enter A New Major:")
            student.set_major(new_input22)


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

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

def main():
    #List of Student Info
    Student_List = []
    while True:
        print("Hello and Welcome!Please pick an option by inputting the number assigned to it:")
        print()
        print("1.Add A Student\n"
          "2.Edit Student Info\n"
          "3.Remove Student\n"
          "4.Display Student\n"
          "5.Exit\n")
        User_Input = int(input("Please Enter Your Option:"))
        if User_Input == 1:
            #Name Information For Classes
            Name_First = input("Please Enter Your First Name:")
            Name_Middle = input("Please Enter Your Middle Name (Type N/A if None):")
            Name_Last = input("Please Enter Your Last Name:")
            Student_ID = int(input("Please Enter Your Student ID:"))
            Unified_Student_Info = Person(Name_First,Name_Middle,Name_Last)

            #Street Info For Classes
            Street_Address = input("Please Enter Your Street Address:")
            City_Name = input("Please Enter Your City:")
            State = input("Please Enter Your State:")
            Zip = input("Please Enter Your ZIP Code:")
            Mailing_Type = input("What Type of Address do you have?(Permanent,Local,etc.):")
            Unified_MailingAddress = MailingAddress(Street_Address,City_Name,State,Zip,Mailing_Type)

            #Email Address Info for Classes
            Email_Address = input("Please Enter Your Email:")
            Email_Type =  input("What Kind Of Email is it?(Academic,Industrial,etc.):")
            Unified_Email = EmailAddress(Email_Address,Email_Type)

            # Phone Number Info for Classes
            Phone_Number =  input("Please Enter Your Phone Number:")
            Phone_Type = input("What Kind Of Phone is it?(Cell,Home,Office):")
            Unified_Phone = Phone(Phone_Number,Phone_Type)

            # Birthday Info for Classes
            Birth_Month = input("Please Enter Your Birth Month:")
            Birth_Day = input("Please Enter Your Birth Day:")
            Birth_Year = input("Please Enter Your Birth Year:")
            Unified_BirthDay = Date(Birth_Year,Birth_Month,Birth_Day)

            #Enrollment Info for Classes
            Enrollment_Date = input("Please Enter Your Enrollment Date (Month/Day/Year):")
            Starting_Semester = input("What Semester And Year are you starting in?:")
            Major = input("What's your major?:")
            Unified_Extra = Student(Student_ID,Enrollment_Date,Starting_Semester,Major)

            Student_List.append(Unified_Student_Info)
            print()

        elif User_Input == 2:
            print("2")
            print()
        elif User_Input == 3:
            print("3")
            print()
        elif User_Input == 4:
            print("4")
            print()
        elif User_Input == 5:
            print("Thank you for using our program!")
            break
        else:
            print("Invalid Number. Please Try Again")




if __name__ == '__main__':
    main()

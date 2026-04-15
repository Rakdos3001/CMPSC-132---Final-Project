# Course class
class Course:
    #Constructor
    def __init__(self, course_number: str, semester_taken: str, delivery:str, status:str, grade:str):
        self.__course_number = course_number
        self.__semester_taken = semester_taken
        self.__delivery = delivery
        self.__status = status
        self.__grade = grade

    #Course Number Setter/Getter
    def set_course_number(self, new_course_number:str):
        self.__course_number = new_course_number

    def get_course_number(self):
        return self.__course_number

    #Semester Taken Setter/Getter
    def set_semester_taken(self, new_semester_taken: str):
        self.__semester_taken = new_semester_taken

    def get_semester_taken(self):
        return self.__semester_taken

    # Delivery Setter/Getter
    def set_delivery(self, new_delivery: str):
        self.__delivery = new_delivery

    def get_delivery(self):
        return self.__delivery

    # Status Setter/Getter
    def set_status(self, new_status: str):
        self.__status = new_status

    def get_status(self):
        return self.__status

    #Grade Setter/getter
    def set_grade(self, new_grade: str):
        self.__grade = new_grade

    def get_grade(self):
        return self.__grade

    #String Overload
    def __str__(self):
        return (f"Course Number: {self.__course_number}"
                f"Semester Taken: {self.__semester_taken}"
                f"Delivery Method: {self.__delivery}"
                f"Status: {self.__status}"
                f"Grade: {self.__grade} ")

# Child of Person, adds infor for student data
from Person import Person
from MailingAddress import MailingAddress
from Phone import Phone
from Date import Date
from EmailAddress import EmailAddress
from Course import Course
from LinkedList import LinkedList

class Student(Person):
	# Constructor
	def __init__(self, student_id: int, name_first: str = None, name_last: str = None, name_middle: str = None,
                 address: MailingAddress = None, emails: list[EmailAddress] = None, phones: list[Phone] = None, birth_date: Date = None,
				 acceptance_date: Date = None, semester_start: Date = None,
				 major: str = "Undeclared", courses: LinkedList = LinkedList()):
		Person.__init__(self, name_first, name_last, name_middle, address, emails, phones, birth_date)
		self.__student_id = student_id
		self.__acceptance_date = acceptance_date
		self.__semester_start = semester_start
		self.__major = major
		self.__courses = courses

	# Setters
	def set_student_id(self, student_id: int):
		self.__student_id = student_id

	def set_acceptance_date(self, acceptance_date: Date):
		self.__acceptance_date = acceptance_date

	def set_semester_start(self, semester_start: Date):
		self.__semester_start = semester_start

	def set_major(self, major: str):
		self.__major = major

	def set_courses(self, courses: LinkedList):
		self.__courses = courses

	# Getters
	def get_student_id(self):
		return self.__student_id

	def get_acceptance_date(self):
		return self.__acceptance_date

	def get_semester_start(self):
		return self.__semester_start

	def get_major(self):
		return self.__major

	def get_courses(self):
		return self.__courses

	# Overloads
	def __eq__(self, other: Student):
		return self.__student_id == other.get_student_id()

	def __lt__(self, other: Student):
		return self.__student_id < other.get_student_id()

	def __gt__(self, other: Student):
		return self.__student_id > other.get_student_id()

	def __str__(self):
		# Traverse courses list and turn into a string
		course_str = ""
		pos = self.__courses.get_head()
		while pos is not None:
			course: Course = pos.get_data()
			course_str += f"{course.get_course_number()}, "

			pos = pos.get_next()
		course_str = course_str.strip(", ")

		return (
        	Person.__str__(self) + "\n"
			f"\tStudent ID: {self.__student_id}\n"
			f"\tAcceptance Date: {self.__acceptance_date}\n"
			f"\tSemester Starts: {self.__semester_start}\n"
			f"\tMajor: {self.__major}\n"
			f"\tCourses: {course_str}"
        )
# Child of Person, adds infor for student data
from Person import Person
from MailingAddress import MailingAddress
from Phone import Phone
from Date import Date
from EmailAddress import EmailAddress

class Student(Person):
	# Constructor
	def __init__(self, student_id: int, name_first: str, name_last: str, name_middle: str = None,
                 address: MailingAddress = None, emails: list[EmailAddress] = None, phones: list[Phone] = None, birth_date: Date = None,
				 acceptance_date: Date = None, semester_start: Date = None, major: str = "Undeclared"):
		Person.__init__(self, name_first, name_last, name_middle, address, emails, phones, birth_date)
		self.__student_id = student_id
		self.__acceptance_date = acceptance_date
		self.__semester_start = semester_start
		self.__major = major

	# Setters
	def set_student_id(self, student_id: int):
		self.__student_id = student_id

	def set_acceptance_date(self, acceptance_date: Date):
		self.__acceptance_date = acceptance_date

	def set_semester_start(self, semester_start: Date):
		self.__semester_start = semester_start

	def set_major(self, major: str):
		self.__major = major

	# Getters
	def get_student_id(self):
		return self.__student_id

	def get_acceptance_date(self):
		return self.__acceptance_date

	def get_semester_start(self):
		return self.__semester_start

	def get_major(self):
		return self.__major
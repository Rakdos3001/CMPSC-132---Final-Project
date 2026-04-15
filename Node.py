
class Node:
	# Constructor
	def __init__(self, data):
		self.__data = data
		self.__next = None # Pointer to next node

	# Setters
	def set_data(self, data):
		self.__data = data

	# Getters
	def get_data(self):
		return self.__data

	# String
	def __str__(self):
		return f"{self.__data}"


class Node:
	# Constructor
	def __init__(self, data, next_node = None):
		self.__data = data
		self.__next = next_node # Pointer to next node

	# Setters
	def set_data(self, data):
		self.__data = data

	# Getters
	def get_data(self):
		return self.__data

	# String
	def __str__(self):
		return f"{self.__data}"

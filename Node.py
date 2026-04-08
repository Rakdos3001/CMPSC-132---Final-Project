class Node:
	# Constructor
	def __init__(self, data, next_node: Node = None):
		self.__data = data
		self.__next = next_node # Pointer to next node

	# Setters
	def set_data(self, data):
		self.__data = data

	def set_next(self, next_node: Node):
		self.__next = next_node

	# Getters
	def get_data(self):
		return self.__data

	def get_next(self):
		return self.__next

	# String
	def __str__(self):
		return str(self.__data)
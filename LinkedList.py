from Node import Node

# Linked list with only a head, no tail
class LinkedList:
    def __init__(self):
        self.__head: Node = None

    def append(self, data):
        # Wrap the data into a node
        new_node = Node(data)

        # Special case: list is empty, set head to new_node
        if self.__head is None:
            self.__head = new_node

        # Traverse to end and set new pointer
        else:
            pos = self.__head
            while pos.get_next() is not None:
                pos = pos.get_next()

            pos.set_next(new_node)

    def search(self, key):
        # Traverse to end
        pos = self.__head

        while pos is not None:
            if pos.get_data() == key:
                # Return if found
                return pos

            # Continue if not found
            pos = pos.get_next()

        # Not found, return None
        return None

    def remove(self, key):
        # Special case: empty
        if self.__head is None:
            return None

        # Special case: remove head
        elif self.__head.get_data() == key:
            save = self.__head
            self.__head = self.__head.get_next()

            return save

        # Normal: Traverse
        pos = self.__head
        next_pos = pos.get_next()

        # Checking next values
        while next_pos is not None:
            # Found: set current node to skip to skip the next node
            if next_pos.get_data() == key:
                save = next_pos
                pos.set_next(next_pos.get_next())

                return save

            # Otherwise continue
            pos = next_pos
            next_pos = pos.get_next()

        # Not found
        return None

    def __str__(self):
        output_str = "["

        # Traverse to end
        pos = self.__head
        while pos is not None:
            # Printing each
            output_str += f"{pos}, "
            pos = pos.get_next()

        # Formatting and return
        output_str = output_str.strip(", ") + "]"

        return output_str

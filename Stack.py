# Stack

from LinkedList import SinglyLinkedList


class Stack:
    def __init__(self):
        self.new_list = SinglyLinkedList()

    def push(self, data):
        self.new_list.prepend()

    def pop(self):
        return self.new_list.remove_from_head()

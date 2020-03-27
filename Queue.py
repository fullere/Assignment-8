from DoubleLink import Double_Linked_List

class Queue:
    def __init__(self):
        self.myList=Double_Linked_List()

    def push(self, data):
        self.myList.push_end(data)

    def pop(self, data):
        return self.myList.pop_head(data)

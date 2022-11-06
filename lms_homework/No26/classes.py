class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class MyStack:
    def __init__(self, first_element=None):
        self.pointer = Node(first_element)  # Head of our Stack with first element

    def push(self, somedata):
        if self.pointer.data is None:
            self.pointer.data = somedata
        else:
            new_noda_h = Node(somedata)  # Creat new Node then push in stakc
            new_noda_h.next = self.pointer  # Link in new Node on old Nodes (Stack)
            self.pointer = new_noda_h  # Head of Stack linking on our new Node

    def __str__(self):
        string_row = ''
        temp = self.pointer
        string_row += str("[")
        while temp.next is not None:
            string_row += str(temp.data)
            if temp.next:
                string_row += str(', ')
            temp = temp.next
        string_row += str(temp.data)
        string_row += str("]")
        return string_row

    def get_print(self, steeps=3):
        for _ in range(steeps):
            returner = self.pointer.data
            self.pointer = self.pointer.next
            print(returner)

    def get(self):
        if self.pointer:
            returner = self.pointer.data
            self.pointer = self.pointer.next
            return returner
        return None

    def get_from_stack(self, finder):
        temp = self.pointer
        while temp:
            if temp.data == finder:
                # print(f'Index [{MyQueue.index}]: {temp.data}')
                return temp.data
            temp = temp.next

        raise ValueError("None element in Stack")


class MyQueue:
    index = 0

    def __init__(self, first_element=None):
        self.pointer = Node(first_element)  # Creat first Node then push in Queue
        self.iterr = 0

    def __str__(self):
        string_row = ''
        if self.pointer.data is not None:
            string_row += '['

            temp = self.pointer
            while temp:
                string_row += str(temp.data)
                if temp.next:
                    string_row += str(', ')
                temp = temp.next

            string_row += str(']')
            return string_row
        return None

    def __iter__(self):
        temp = self.pointer
        while temp:
            yield temp.data
            temp = temp.next

    def push(self, somedata):
        if self.pointer.data is None:
            self.pointer.data = somedata  # Creat first Node then push in Queue if obj is void
        else:
            temp = self.pointer
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(somedata)  # Creat new Node then push in Queue
            MyQueue.index += 1

    def get_from_queue(self, finder):
        temp = self.pointer
        while temp:
            if temp.data == finder:
                # print(f'Index [{MyQueue.index}]: {temp.data}')
                return temp.data
            temp = temp.next

        raise ValueError("None element in Queue")

    def get_item_index(self, index):
        count_index = 0
        temp = self.pointer
        while temp:
            if index == count_index:
                return temp.data
            temp = temp.next
            count_index += 1
        raise IndexError("Over index")

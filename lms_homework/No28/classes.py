class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class MyUnorderedList:

    def __init__(self, first_element=None):
        self.pointer = Node(first_element)  # Creat first Node then push in Queue

        if first_element is None:
            self.lenght = 0
        else:
            self.lenght = 1

    def __str__(self):
        string_row = ''
        if self.pointer.data is not None:
            string_row += '['

            temp = self.pointer
            while temp:
                if type(temp.data) is str:
                    string_row += "'" + str(temp.data) + "'"
                else:
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

    def __len__(self):
        return self.lenght

    def __getitem__(self, item):
        lister = []
        temp = self.pointer
        while temp:
            lister.append(temp.data)
            temp = temp.next

        if isinstance(item, slice):
            return lister[item.start:item.stop:item.step]
        else:
            return lister[item]

    def append(self, somedata):
        if self.pointer.data is None:
            self.pointer.data = somedata  # Creat first Node then push in Queue if obj is void

        else:
            temp = self.pointer
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(somedata)  # Creat new Node then push in Queue

        self.lenght += 1

    def remove(self, somedata):
        now_node = self.pointer
        prev_node = None

        while now_node.data:
            if now_node.data == somedata:

                if prev_node:
                    prev_node.next = now_node.next
                else:
                    self.pointer = now_node.next
                self.lenght -= 1
                print(f'Done! remove {somedata}')
                return True
            else:
                prev_node = now_node
                now_node = now_node.next

        print(f'Error! not element {somedata} in list')
        return False

    def pop(self, index: int = None):
        if index is None:
            prev_temp = None
            temp = self.pointer
            while temp.next:
                prev_temp = temp
                temp = temp.next
            prev_temp.next = None
            return temp.data

        if type(index) is not int:
            raise TypeError("Method 'index' must be only integer")
        if index > self.lenght:
            raise Exception("'index' must be in range length our list")

        if self.pointer:
            point = 1
            now_node = self.pointer
            prev_node = None

            while now_node:
                if point == index:
                    result = now_node.data

                    if prev_node:
                        prev_node.next = now_node.next
                    else:
                        self.pointer = now_node.next
                    self.lenght -= 1
                    return result
                else:
                    prev_node = now_node
                    now_node = now_node.next

                point += 1

        return False


class MyStack:
    """"
    Method LIFO
    """

    def __init__(self, first_element=None):
        self.pointer = Node(first_element)  # Head of our Stack with first element

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

    def push(self, somedata):
        if self.pointer.data is None:
            self.pointer.data = somedata
        else:
            new_noda_h = Node(somedata)  # Creat new Node then push in stakc
            new_noda_h.next = self.pointer  # Link in new Node on old Nodes (Stack)
            self.pointer = new_noda_h  # Head of Stack linking on our new Node

    def pop(self):
        """
        return and del first value
        """
        out = self.pointer.data
        self.pointer = self.pointer.next
        return out


class MyQueue:
    """"
    Method FIFO
    """
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
        """
        push in end position
        """
        if self.pointer.data is None:
            self.pointer.data = somedata  # Creat first Node then push in Queue if obj is void
        else:
            temp = self.pointer
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(somedata)  # Creat new Node then push in Queue
            MyQueue.index += 1

    def pop(self):
        """
        return and del first value
        """
        out = self.pointer.data
        self.pointer = self.pointer.next
        return out

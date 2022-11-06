from classes import Node, MyStack, MyQueue


def revers_row(base_row):
    new_row = ''
    stack = MyStack()

    for symbol in base_row:
        stack.push(symbol.lower())

    temp = stack.pointer
    while temp.next is not None:
        new_row += str(temp.data)
        temp = temp.next
    new_row += str(temp.data)
    return new_row.title()


def balanced(row):
    opened = 0
    closed = 0

    new_list = MyQueue()
    for element in row:
        new_list.push(element)

    if new_list.get_item_index(0) == ')':
        return False

    for element in new_list:
        if element == '(':
            opened += 1
        else:
            closed += 1

    if opened == closed:
        return True
    return False


if __name__ == "__main__":

    #'Task 1'
    test_line = 'Dracula'
    print(revers_row(test_line))

    # 'Task 2'
    print(balanced(')'))
    print(balanced('(())'))
    print(balanced('(()()())()(())'))
    print(balanced('(()))'))
    print(balanced('(())('))
    print(balanced('((())'))

    # 'Task 3.1'
    stack = MyStack(0)
    stack.push('one')
    stack.push('two')
    stack.push('three')
    print(f"Stack: {stack}")
    print("Find of stack: ", stack.get_from_stack(0))

    # 'Task 3.2'
    print()
    arr = MyQueue(0)
    arr.push('one')
    arr.push('two')
    arr.push('three')
    print(f"Queue: {arr}")
    print("Find of Queue: ", arr.get_from_queue('three'))
    print("Find of index in Queue: ", arr.get_item_index(3))
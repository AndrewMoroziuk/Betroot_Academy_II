from classes import MyUnorderedList, MyStack, MyQueue


#


if __name__ == '__main__':
    # Task 1
    arr = MyUnorderedList(1)
    # arr.append("2")
    # arr.append(3)
    # arr.append(4)
    # arr.append(5)
    #
    # print(arr, '    Length:', len(arr))
    #
    # arr.remove(3)
    # print(arr, '    Length:', len(arr))
    #
    # print('POP element:', arr.pop())
    # print(arr, '    Length:', len(arr))
    #
    # arr.append(3)
    # arr.append(4)
    # arr.append(5)
    # arr.append(3)
    # arr.append(4)
    # arr.append(5)
    # print(arr.pop())
    # print(arr, '    Length:', len(arr))
    #
    # a = arr[2:7:2]
    # print(a)

    # Task 2
    stack = MyStack(0)  # власна реалізація Стеку
    print(stack)
    stack.push(1)
    print(stack)
    stack.push(2)
    print(stack)

    stack.pop()
    print(stack)

    stack.push(2)
    print(stack)

    # Task 3
    queue = MyQueue(0)  # власна реалізація Черги
    for i in range(1, 15):
        queue.push(i)
        print(queue)

    for i in range(5):
        queue.pop()
        print(queue)

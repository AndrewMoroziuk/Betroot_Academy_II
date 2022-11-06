import datetime


class MyBubbleSort:
    def __init__(self, arr):
        self.__arr = arr
        self.length = len(arr)
        self.count_time = None

        for elem in self.__arr:
            if type(elem) is int:
                continue
            raise ValueError("Type value not int or float")

    def sorted(self, revers=False):
        temp_start_time = datetime.datetime.now()

        swapped = False
        for each_element in range(self.length):
            for index_element in range(0, self.length - each_element - 1):

                if revers is False:
                    if self.__arr[index_element] > self.__arr[index_element + 1]:
                        self.__arr[index_element], self.__arr[index_element + 1] = (
                            self.__arr[index_element + 1],
                            self.__arr[index_element],
                        )
                        swapped = True
                else:
                    if self.__arr[index_element] < self.__arr[index_element + 1]:
                        self.__arr[index_element], self.__arr[index_element + 1] = (
                            self.__arr[index_element + 1],
                            self.__arr[index_element],
                        )
                        swapped = True

            if swapped is False:
                break

        temp_end_time = datetime.datetime.now()
        self.count_time = temp_end_time - temp_start_time

    def printl(self):
        print(*self.__arr)
        print(f"Time processing: {self.count_time}\n")


if __name__ == "__main__":
    a = MyBubbleSort([64, 34, 25, 12, 11, 90, 64, 34, 25, 12, 11])
    a.sorted(True)
    a.printl()

    a.sorted()
    a.printl()

    a = MyBubbleSort([64, 34, 25, 12, "11", 90, 64, 34, 25, 12, 11])
    a.sorted(True)
    a.printl()

import itertools


# Task 1 TasK 2
class InRange:
    def __init__(self, cursorer, end, step=1):
        self.cursor = cursorer
        self.end = end
        self.step = step
        self.list_slice = []

    def __repr__(self):
        return f'\'Обєкт власного класу InRange\''

    def __iter__(self):
        self.a = itertools.count(start=1)
        return self

    def __next__(self):
        if self.cursor >= self.end:
            raise StopIteration
        self.cursor += self.step
        return self.cursor - self.step, self.a.__next__()

    def __getitem__(self, cursore):

        while self.cursor < self.end:
            self.cursor += self.step
            self.list_slice.append(self.cursor - self.step)
        return self.list_slice[cursore]


for value, number in InRange(1, 20, 3):
    print(f'Значення {value}, порядковий номер {number}')

print()

a = InRange(1, 20, 3)
print(a)
print(a[2:5])
print(a[3:5])
print(a[5:3:-1])
print(a.__dict__)


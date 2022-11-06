# Task 1
# Implement binary search using recursion.


# Task 2
# Read about the Fibonacci search and implement it using python. Explore its complexity and compare it to sequential, binary searches.

# Task 3
# Implement in (__contains__) len (__len__) methods for HashTable
# C:\Users\rnaku\Desktop\beetroot\code\graphs\homeworks.py


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                next_slot = self.re_hash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.re_hash(next_slot, len(self.slots))

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    @staticmethod
    def hash_function(key, size):
        return key % size

    @staticmethod
    def re_hash(old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.re_hash(position, len(self.slots))
                if position == start_slot:
                    stop = True

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


if __name__ == "__main__":
    Hasher = HashTable()
    Hasher[54] = "cat"
    Hasher[26] = "dog"
    Hasher[93] = "lion"
    Hasher[17] = "tiger"
    Hasher[77] = "bird"
    Hasher[31] = "cow"
    Hasher[44] = "goat"
    Hasher[55] = "pig"
    Hasher[20] = "chicken"
    print(Hasher.slots)
    print(Hasher.data)

    print(Hasher[20])

    print(Hasher[17])
    Hasher[20] = "duck"
    print(Hasher[20])
    print(Hasher[99])

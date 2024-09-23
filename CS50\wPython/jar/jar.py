class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if not (type(n) == int and n > 0):
            raise ValueError("Invalid input type")
        if self.size + n > self.capacity:
            raise ValueError("The jar can't fit that many cookies")
        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("There aren't that many cookies")
        self.size -= n

    # getter
    @property
    def capacity(self):
        return self._capacity

    # setter
    @capacity.setter
    def capacity(self, capacity):
        if not (type(capacity) == int and capacity >= 0):
            raise ValueError("Invalid capacity")
        self._capacity = capacity

    # getter
    @property
    def size(self):
        return self._size

    # setter
    @size.setter
    def size(self, size):
        if not (type(size) == int and size >= 0):
            raise ValueError("Invalid number of cookies")
        self._size = size

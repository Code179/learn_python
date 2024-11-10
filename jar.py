def main():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(7)
    print(jar)

class Jar:

    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        try:
            if n > self._capacity:
                raise ValueError("Too many cookies")
            elif self._size + n > self._capacity:
                raise ValueError("Jar is already full")
            elif n < 0:
                raise ValueError("Negativ amount of cookies is impossible")
        except ValueError as e:
            print(e)
            raise
        self._size += n

    def withdraw(self, n):
        try:
            if self._size < n:
                raise ValueError("Not enough cookies")
            self.size -= n
        except ValueError as e:
            print(e)
            raise

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity must be non-negative")
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        self._size = size
        """if size < 0:
            raise ValueError("Size must be non-negative")
        self._size = size"""
    

if __name__ == "__main__":
    main()
import random

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0  # Number of key-value pairs

        # Parameters for universal hashing
        self.p = 10**9 + 7  # Large prime number
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)

    def _hash(self, key):
        h = hash(key)
        return ((self.a * h + self.b) % self.p) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        # Check if key exists; update if so
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # Else, insert new
        self.table[index].append((key, value))
        self.count += 1
        self._check_load_factor()

    def search(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # Not found

    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                self.count -= 1
                return True
        return False  # Key not found

    def _check_load_factor(self):
        load_factor = self.count / self.size
        if load_factor > 0.75:
            self._resize()

    def _resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0

        # Generate new universal hash parameters
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)

        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

    def __str__(self):
        return str(self.table)

if __name__ == "__main__":
    ht = HashTable()

    ht.insert("apple", 1)
    ht.insert("banana", 2)
    ht.insert("orange", 3)

    print("Search 'banana':", ht.search("banana"))
    ht.delete("banana")
    print("Search 'banana' after deletion:", ht.search("banana"))

    print("Current Hash Table:")
    print(ht)


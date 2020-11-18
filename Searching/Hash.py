class HashTable:
    def __init__(self, size=50):
        if size <= 0:
            print("Size must be more than 0: Change to default size(50)")
            self.size = 50
        else:
            self.size = size
        self.table = []
        for _ in range(self.size):  # use separate chaining (use more memory but will make no collision)
            self.table.append([])

    def get_hash(self, key):
        _magic = 2654435761
        if type(key) is int:
            return key*_magic % self.size
        elif type(key) is str:
            number = 0
            for character in key:
                number += ord(character)
            return number*_magic % self.size
        elif type(key) is float:
            return int(key * _magic) % self.size
        else:
            return key*_magic % self.size

    def element_size(self):
        size = 0
        for lst in self.table:
            size += len(lst)
        return size

    def load_factor(self):
        return self.element_size()/self.size

    def insert(self, value):
        self.table[self.get_hash(value)].append(value)
        # TODO: resizing procedure (Look at Rehashing Grader code)

    def pop_value(self, value):
        _, lst = self.search(value)
        if lst is None:
            print("Value don't exist")
            return
        return lst.pop_value(lst.index(value))

    def search(self, key):
        index = self.get_hash(key)
        if len(self.table[index]) > 0:
            lst = self.table[index]
            for i in range(len(lst)):
                if key == lst[i]:
                    return index, lst
            return -1, None
        return -1, None

    def __str__(self):
        out = ''
        for item in self.table:
            if len(item) > 0:
                out += str(item) + ' '
        return out


if __name__ == '__main__':
    hash_table = HashTable(10)
    value_lst = [12, 365, 20, 51, 'abc', 5615, 3.14159, 3, 8156, 99, 123, 6, 510, 256]
    for value in value_lst:
        hash_table.insert(value)
    print(hash_table)
    key_lst = [365, 12, 20, 541, 51, 5615, 256]
    for key in key_lst:
        print(hash_table.search(key)[0], end=' ')
    print()
    print(hash_table.pop_value(365))
    print(hash_table.pop_value('abc'))
    print(hash_table.pop_value(3.14159))
    hash_table.insert(3.9415)
    print(hash_table)
    print(hash_table.element_size())
    print(hash_table.load_factor())

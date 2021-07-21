class HashTable:
    __items = [[] for _ in range(32)]

    def __get_index(self, key):
        return hash(key) % len(self.__items)

    def put(self, key, value):
        idx = self.__get_index(key)
        assert 0 <= idx < len(self.__items)
        for i, (k, v) in enumerate(self.__items[idx]):
            if k == key:
                self.__items[idx][i] = (key, value)
                return
        self.__items[idx].append((key, value))

    def get(self, key):
        idx = self.__get_index(key)
        for k, v in self.__items[idx]:
            if k == key:
                return v
        return None


if __name__ == '__main__':
    table = HashTable()
    table.put('abc', 42)
    table.put('abc', 31337)
    table.put('d', 1)
    print(f'abc={table.get("abc")}')
    print(f'd={table.get("d")}')
    print(f'qwe={table.get("qwe")}')

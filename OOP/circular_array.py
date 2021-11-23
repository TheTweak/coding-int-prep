'''
Implement a circular array, that can rotate efficiently.
'''

class CircularArray:
    def __init__(self, data):
        self.data = data
        self.head = 0
        self.iter_ptr = 0

    def rotate(self, times: int = 1) -> None:
        t = times % len(self.data)
        if t == 0:
            return

        self.head += 1
        if self.head == len(self.data):
            self.head = 0

    def __convert_idx(self, i) -> int:
        if i < 0 or i >= len(self.data):
            raise IndexError("index out of bounds")

        start = len(self.data) - self.head
        return (start+i)%len(self.data)

    def __getitem__(self, i):
        return self.data[self.__convert_idx(i)]

    def __setitem__(self, i, value):
        self.data[self.__convert_idx(i)] = value

    def __iter__(self):
        self.iter_ptr = 0
        return self

    def __next__(self):
        if self.iter_ptr >= len(self.data):
            raise StopIteration()

        item = self[self.iter_ptr]
        self.iter_ptr += 1
        return item


if __name__ == '__main__':
    ca = CircularArray([1, 2, 3])
    ca[0] = 0
    print([x for x in ca])
    ca.rotate(1)
    ca[1] = 1
    print([x for x in ca])
    ca.rotate(1)
    print([x for x in ca])
    ca.rotate(1)
    print([x for x in ca])

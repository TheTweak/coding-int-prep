'''
Implement a queue using two stacks.

push: O(N)=N time and space
pop: O(N)=1


Improvement:
    use lazy push: do not move elements around until pop is performed.
'''

class Stack:
    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        result = self.data[-1]
        del self.data[-1]
        return result

    def is_empty(self) -> bool:
        return len(self.data) == 0


class Queue:
    def __init__(self):
        self.stack_newest = Stack()
        self.stack_oldest = Stack()

    def push(self, x: int) -> None:
        self.stack_newest.push(x)

    def pop(self) -> int:
        if self.stack_oldest.is_empty():
            while not self.stack_newest.is_empty():
                self.stack_oldest.push(self.stack_newest.pop())
        return self.stack_oldest.pop()


if __name__ == '__main__':
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    assert q.pop() == 1
    assert q.pop() == 2
    q.push(5)
    assert q.pop() == 3

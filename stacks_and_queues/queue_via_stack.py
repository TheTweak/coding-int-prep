'''
Implement a queue using two stacks.

push: O(N)=N time and space
pop: O(N)=1
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
        self.stack_a = Stack()
        self.stack_b = Stack()

    def push(self, x: int) -> None:
        while not self.stack_b.is_empty():
            self.stack_a.push(self.stack_b.pop())
        self.stack_b.push(x)
        while not self.stack_a.is_empty():
            self.stack_b.push(self.stack_a.pop())

    def pop(self) -> int:
        return self.stack_b.pop()


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

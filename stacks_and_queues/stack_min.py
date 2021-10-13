'''
Design a stack, that has min() operation, that returns minimum element.
pop(), push(), min() should work in O(1) time.

brute force:
    maintain a second internal stack for min elements.

    push():
    if stack_min is empty - push element onto it.
    if stack_min is not empty, compare current element with top element in stack_min:
        - if element <= stack_min top, push element onto stack_min
        - otherwise do nothing

    pop():
    if popped element == top of min_stack, also pop from min_stack
'''
from collections import deque

class MinStack():
    def __init__(self):
        self.stack = deque()
        self.min_stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.min_stack):
            if x <= self.min_stack[-1]:
                self.min_stack.append(x)
        else:
            self.min_stack.append(x)

    def pop(self) -> int:
        if len(self.stack):
            x = self.stack.pop()
            if len(self.min_stack):
                if x == self.min_stack[-1]:
                    self.min_stack.pop()
            return x
        return None

    def min(self) -> int:
        if len(self.min_stack):
            return self.min_stack[-1]
        return None


if __name__ == '__main__':
    ms = MinStack()
    ms.push(5)
    assert ms.min() == 5
    ms.push(0)
    assert ms.min() == 0
    ms.pop()
    assert ms.min() == 5
    ms.push(10)
    assert ms.min() == 5
    ms.push(1)
    assert ms.min() == 1
    ms.push(0)
    assert ms.min() == 0

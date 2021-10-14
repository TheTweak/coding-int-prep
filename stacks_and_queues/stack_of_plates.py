'''
Implement a data structure, that consists of a set of stacks.
Each time a stack exceeds capacity threshold, a new stack should be
allocated. push() and pop() should behave as it was a single stack.

brute force:
    maintain a stack of stacks (main stack). when stack exceeds threshold, add another one to the top.
    when stack becomes empty, remove it from main stack.
    pop()/push() is applied to the top stack of the main stack.

    time: O(N)=1
    space: O(N)=N


Follow up:
    implement a function pop_at(i) that pops from a specific stack

    use a list for the main_stack.
    when middle stack becomes empty, pop the stack, moving down all
    other stacks

    time: O(N)=N

'''
from collections import deque

class SetOfStacks:
    def __init__(self, threshold=3):
        self.main_stack = []
        self.threshold = threshold

    def push(self, x: int) -> None:
        if len(self.main_stack) == 0 or len(self.main_stack[-1]) >= self.threshold:
            self.main_stack.append(deque())

        self.main_stack[-1].append(x)

    def pop(self) -> int:
        if len(self.main_stack) == 0:
            return None

        if len(self.main_stack[-1]) == 0:
            del self.main_stack[-1]

        if len(self.main_stack) == 0:
            return None

        return self.main_stack[-1].pop()

    def pop_at(self, i: int) -> int:
        result = self.main_stack[i].pop()
        if len(self.main_stack[i]) == 0:
            del self.main_stack[i]
        return result


if __name__ == '__main__':
    s = SetOfStacks()
    s.push(0)
    s.push(0)
    s.push(0)
    s.push(0)
    assert len(s.main_stack) == 2
    s.pop()
    s.pop()
    assert len(s.main_stack) == 1
    s.push(1)
    s.push(0)
    s.push(0)
    s.push(0)
    s.push(0)
    s.push(0)
    assert len(s.main_stack) == 3
    assert s.pop_at(0) == 1


'''
Implement a function to sort a stack, such that smallest elements are on top.
Not allowed to use list/set or any other collection except temp stack.
stack supports push() pop() peek() is_empty()

brute force:
    3 1 4 2 5 7

    3 1 4 2 5
    7

    3 1 4 2
    7 5

    3 1 4
    7 5 2

    3 1 2
    7 5 4

    3 1
    7 5 4 2

    3
    7 5 4 2 1

    1 2
    7 5 4 3

    7 5 4 3 2 1
    
    O(N)=n^2

    while main stack is not empty:
    1.pop() x from main stack
    2.while x > tmp.peek(), pop from tmp and push to main
    3.push x to tmp

'''
from collections import deque

def sort_stack(stack: deque) -> None:
    tmp = deque()
    while len(stack) != 0:
        tmp.append(stack.pop())

    while len(tmp) != 0:
        x = tmp.pop()
        while len(stack) and x > stack[-1]:
            tmp.append(stack.pop())
        stack.append(x)


if __name__ == '__main__':
    stack = deque()
    stack.append(1)
    stack.append(2)
    stack.append(0)
    stack.append(3)
    stack.append(7)
    stack.append(8)
    sort_stack(stack)
    print(*stack)


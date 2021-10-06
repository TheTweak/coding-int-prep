'''
You have 2 numbers, each of them is represented as a linked list, with digits
in reverse order (1's are head). Implement a function that returns their sum
as a linked list in the same format.

EX: (7 -> 1 -> 6) + (5 -> 9 -> 2) = (2 -> 1 -> 9)
617 + 295 = 912

Follow up: Suppose now the digits are stored in the forward order.
'''

class Node:
    
    def __init__(self):
        self.next = None
        self.value = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, value: int) -> Node:
        if not self.head:
            self.head = Node()
            self.head.value = value
            return self.head
        else:
            tail = self.head
            while tail.next:
                tail = tail.next
            tail.next = Node()
            tail.next.value = value
            return tail.next


'''
brute force:
    starting from head:
    - read digit from node of each list
    - add them together
    - add the overflow (if available)
    - if result is two digit, save the second digit (overflow)
    - append the other digit to the resulting linked list
    - if one list is longer, append the rest of the list to result

    in the end, append the overflow to the resulting list, if available

    time: O(n)=len_longest
    space: O(n)=len_longest for the resulting linked list

    if digits are stored in forward order:

    - reverse the lists first
    - reverse the result

    improvement: use one of the linked lists to store the result

'''


def reverse(l: LinkedList) -> None:
    assert l.head
    prev = None
    nxt = None
    n = l.head
    while n:
        nxt = n.next
        n.next = prev
        prev = n
        n = nxt
    l.head = prev


def sum_lists(a: LinkedList, b: LinkedList) -> LinkedList:
    reverse(a)
    reverse(b)
    result = LinkedList()
    overflow = False
    n = a.head
    m = b.head
    while n or m:
        s = 0
        if n:
            s += n.value
            n = n.next
        if m:
            s += m.value
            m = m.next
        if overflow:
            s += 1
            overflow = False
        if s // 10:
            overflow = True
            result.add(s%10)
        else:
            result.add(s)

    if overflow:
        result.add(1)

    reverse(result)
    return result


if __name__ == '__main__':
    a = LinkedList()
    a.add(9)
    a.add(9)
    a.add(3)
    '''
    reverse(a)
    n = a.head
    while n:
        print(n.value)
        n = n.next
    '''

    b = LinkedList()
    b.add(7)

    s = sum_lists(a, b)

    n = s.head
    while n:
        print(n.value)
        n = n.next

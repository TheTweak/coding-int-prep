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
        self.size = 0

    def add(self, value: int) -> Node:
        self.size += 1
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

    improvement: use longest of the linked lists to store the result

    1->2->3

    1->4
    
    2->6->3

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
    overflow = False
    a_is_longer = True
    if b.size > a.size:
        a_is_longer = False
    n = a.head
    m = b.head
    while n or m:
        s = 0
        if n:
            s += n.value
        if m:
            s += m.value
        if overflow:
            s += 1
            overflow = False
        if s // 10:
            overflow = True
            if a_is_longer:
                n.value = s%10
            else:
                m.value = s%10
        else:
            if a_is_longer:
                n.value = s
            else:
                m.value = s
        if n:
            n = n.next
        if m:
            m = m.next

    if overflow:
        if a_is_longer:
            a.add(1)
        else:
            b.add(1)

    if a_is_longer:
        reverse(a)
        return a
    else:
        reverse(b)
        return b


if __name__ == '__main__':
    a = LinkedList()
    a.add(1)
    a.add(3)
    a.add(2)
    '''
    reverse(a)
    n = a.head
    while n:
        print(n.value)
        n = n.next
    '''

    b = LinkedList()
    b.add(2)
    b.add(2)
    b.add(1)
    b.add(1)

    s = sum_lists(a, b)

    n = s.head
    while n:
        print(n.value)
        n = n.next

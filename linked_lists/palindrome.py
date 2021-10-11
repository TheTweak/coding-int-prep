'''
Check if a linked list is a palindrome.
'''

class Node:
    
    def __init__(self):
        self.next = None
        self.value = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, value: str) -> Node:
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


'''
questions to ask the interviewer:
    - is list doubly or single linked?

brute force:
    1. find middle node (exclude middle element if size is odd)
    2. reverse the list that starts from this middle node
    3. nodes from beggining to the middle of original list must 
    be equal to the nodes from beggining to the end of reversed half

    O(n) time is n
    O(n) space is 1

improvements:
    1. get rid of reversed list

if list is doubly linked, then it is possible to go from both ends
and compare elements until pointers meet in the middle.
'''
def is_palindrome(ll: LinkedList) -> bool:
    mid = ll.size // 2
    is_odd = ll.size % 2 != 0

    mid_node = ll.head
    for _ in range(mid):
        mid_node = mid_node.next
    if is_odd:
        mid_node = mid_node.next

    half = LinkedList()
    half.head = mid_node
    reverse(half)

    n = half.head
    m = ll.head
    while n:
        if n.value != m.value:
            return False
        n = n.next
        m = m.next
    return True


if __name__ == '__main__':
    ll = LinkedList()
    ll.add('c')
    ll.add('a')
    ll.add('t')
    ll.add('t')
    ll.add('a')
    ll.add('c')
    n = ll.head
    while n:
        print(n.value)
        n = n.next

    print(is_palindrome(ll))


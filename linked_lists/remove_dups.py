'''
Write code to remove duplicates from an unsorted linked list.

What if you can't use a temp buffer?
'''

class Node:
    
    def __init__(self):
        self.next = None
        self.value = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, value: int) -> None:
        if not self.head:
            self.head = Node()
            self.head.value = value
        else:
            tail = self.head
            while tail.next:
                tail = tail.next
            tail.next = Node()
            tail.next.value = value


def remove_dups(ll: LinkedList) -> None:
    '''
    brute force: maintain a set of unique elements,
    remove element if in unique
    time O(n): n
    space O(n): n
    '''
    unique = set()
    n = ll.head
    prev = None
    while n:
        if n.value in unique:
            prev.next = n.next
        else:
            unique.add(n.value)
            prev = n
        n = n.next


'''
time O(n)=n^2
space O(n)=1
'''
def remove_dups_no_buffer(ll: LinkedList) -> None:
    n = ll.head
    while n:
        m = ll.head
        prev = None
        while m:
            if n is not m and n.value == m.value:
                prev.next = m.next
            else:
                prev = m
            m = m.next
        n = n.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.add(1)
    ll.add(1)
    ll.add(2)
    ll.add(2)
    ll.add(2)
    ll.add(5)
    ll.add(5)
    ll.add(2)
    remove_dups_no_buffer(ll)
    n = ll.head
    while n:
        print(n.value)
        n = n.next


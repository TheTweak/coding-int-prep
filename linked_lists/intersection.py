'''
Check if two singly linked lists intersect (have equal nodes, not just values).
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


def print_list(l: LinkedList) -> None:
    n = l.head
    while n:
        print(n.value)
        n = n.next


'''
brute force:
    O(mn) solution to check each node in A vs each
    node in B

intersection in the end:
    a -> b -> c
    d -> c
intersection in the middle:
    a -> b -> c
    x -> f -> b -> c
intersection in the beginning:
    a -> b -> c
    a -> b -> c

-----------
1) copy list A
2) go over list B and change all values
3) go over list A and compare with copy, if some node changed
then it is the intersection point with B

time: O(N+M)
space: O(N)
-----------

'''
def intersect(a: LinkedList, b: LinkedList) -> Node:
    a_copy = LinkedList()
    n = a.head
    while n:
        a_copy.add(n.value)
        n = n.next

    n = b.head
    while n:
        n.value += 'd'
        n = n.next

    n = a.head
    m = a_copy.head
    intersection = None

    while n and m:
        if n.value != m.value:
            intersection = n
            break
        n = n.next
        m = m.next

    return intersection


if __name__ == '__main__':
    ll = LinkedList()
    ll.add('c')
    a = ll.add('a')

    ll2 = LinkedList()
    ll2.head = a
    ll2.add('d')
    print_list(ll2)
    print()
    print_list(ll)

    intersection = intersect(ll, ll2)
    if intersection:
        print(intersection.value)


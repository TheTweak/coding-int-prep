'''
Check if a linked list contains a loop. Return the beginning of the lope node.
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


'''
brute force:
    keep a dict/set of visited nodes, if node is seen again, then there is a loop

    time: O(N)=N
    space: O(N)=N

---
space improvement: if list size is known, go over the list and keep a counter
if counter > list size, then there is a loop

space: O(N)=1
'''
def check_loop(ll: LinkedList) -> Node:
    visited = set()
    n = ll.head
    while n:
        if id(n) in visited:
            return n
        visited.add(id(n))
        n = n.next
    return None


def check_loop_size(ll: LinkedList) -> Node:
    i = ll.size
    n = ll.head
    while n:
        if i < 0:
            return n.next
        n = n.next
        i -= 1
    return None

def check_loop_2_pointers(ll: LinkedList) -> Node:
    fast = ll.head
    slow = ll.head

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            print('collision')
            break

    if not fast:
        return None

    slow = ll.head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.add('a')
    ll.add('b')
    c = ll.add('c')
    d = ll.add('d')
    d.next = c

    loop = check_loop_2_pointers(ll)
    if loop:
        print(f'loop detected: {loop.value}')


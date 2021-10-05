'''
Partition a linked list around a value x, such that all values < x come in the LL
before all the values >= x; x can appear anywhere in the right partition.
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

def update_nodes(head: Node, tail: Node, n: Node) -> (Node, Node):
    if tail:
        tail.next = n
    tail = n
    if not head:
        head = tail
    return head, tail


'''
brute force:

    iterate over linked list, joining together all elements < x
    and everything else in a second linked list
    then join first linked list with second one.

    time O(n)=n
    space O(n)=1 if LL is implemented as just a head node ref
'''
def partition(x: int, ll: LinkedList) -> LinkedList:
    lt_tail = None
    lt_head = None
    ge_tail = None
    ge_head = None
    n = ll.head
    while n:
        if n.value < x:
            lt_head, lt_tail = update_nodes(lt_head, lt_tail, n)
        else:
            ge_head, ge_tail = update_nodes(ge_head, ge_tail, n)
        n = n.next
    if ge_tail:
        ge_tail.next = None
    if lt_tail:
        lt_tail.next = ge_head
    result = LinkedList()
    result.head = lt_head
    if not result.head:
        result.head = ge_head
    return result


if __name__ == '__main__':
    ll = LinkedList()
    ll.add(1)
    ll.add(15)
    ll.add(16)
    ll.add(17)
    ll.add(3)
    ll.add(0)
    ll.add(2)
    ll.add(8)
    ll.add(5)
    ll.add(7)
    ll.add(10)
    ll.add(3)
    n = ll.head
    while n:
        print(n.value)
        n = n.next
    print('---')
    ll = partition(8, ll)
    n = ll.head
    while n:
        print(n.value)
        n = n.next


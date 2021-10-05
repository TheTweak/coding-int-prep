'''
Write code to remove middle element from the singly LL, given only access to that node.
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
a -> b -> c -> d -> e

delete(c)

c.value = d.value
c.next = d.next

a -> b -> d -> e


'''
def delete_mid_node(n: Node) -> None:
    assert n.next
    n.value = n.next.value
    n.next = n.next.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.add(1)
    node = ll.add(2)
    ll.add(4)
    ll.add(7)
    delete_mid_node(node)
    n = ll.head
    while n:
        print(n.value)
        n = n.next


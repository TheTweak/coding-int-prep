from collections import deque
'''
Write code to find k-th to last element in a singly linked list.
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


'''
Maintain a bounded queue of size k, traverse the LL and return last element of the queue.
time O(n)=n
space O(n)=1 (k)
'''
def get_k_to_last(ll: LinkedList, k: int) -> None:
    kq = deque(maxlen=k)
    n = ll.head
    while n:
        kq.append(n)
        n = n.next
    assert len(kq) > 0
    return kq.popleft()


if __name__ == '__main__':
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(4)
    ll.add(7)
    print(get_k_to_last(ll, 4).value)


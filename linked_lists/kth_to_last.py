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


'''
Maintain two pointers k length apart.
time O(n)=n
space O(n)=1
'''
def get_k_to_last_point(ll: LinkedList, k: int) -> None:
    p1 = ll.head
    while p1 and k > 0:
        p1 = p1.next
        k -= 1

    if k != 0:
        return None

    n = ll.head
    m = p1
    while n and m:
        n = n.next
        m = m.next

    return n


'''
a -> b -> c -> d, k=1

d, 1, 0
c, 1, 1
b, 1, 2
a, 1, 3

'''

def get_k_to_last_recursive(x: Node, k: int, counter: list) -> Node:
    if not x:
        return None

    result = get_k_to_last_recursive(x.next, k, counter)
    counter[0] += 1
    if counter[0] == k:
        return x
    return result

if __name__ == '__main__':
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(4)
    ll.add(7)
    counter = [0]
    print(get_k_to_last_recursive(ll.head, 2, counter).value)


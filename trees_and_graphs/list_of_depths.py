'''
Given a binary tree, design an algorithm, which creates a linked list of all nodes
at each level. E.g. for a tree of height H, there will be H linked lists.

brute force:
0) create an array of length log(N)+1 of linked lists
1) run BFS from the root, add pairs of (level, node) to the queue
2) when processing a node, append it to the linked list according to its level

O(N):
    time: N
    space: N
'''

from minimal_tree import create_bs_tree
from collections import deque
import math

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


def create_list_of_depths(btree, n: int) -> list:
    result = [LinkedList() for _ in range(math.ceil(math.log2(n))+1)]
    queue = deque()
    queue.append((0, btree))
    while len(queue):
        level, node = queue.popleft()
        if not node:
            continue
        result[level].add(node.value)
        queue.append((level+1, node.left))
        queue.append((level+1, node.right))
    return result


if __name__ == '__main__':
    n = 31
    btree = create_bs_tree(list(range(n)))
    lists = create_list_of_depths(btree, n)
    for ll in lists:
        n = ll.head
        while n:
            print(n.value, end='->' if n.next else '')
            n = n.next
        print()

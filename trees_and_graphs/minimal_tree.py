'''
Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with min height.

brute force:

min height of such tree is log(N)+1
as the array is sorted, then root element is the middle one
its left child is the middle of (0, root), its right child is (root, N)
and so on.

O(N)=log(N) time and memory
'''

import math
from collections import deque

class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def print_tree(root: Node, n: int) -> None:
    queue = deque()
    queue.append((0, root))
    prev_level = 0
    tree_width = int(math.pow(2, math.ceil(math.log2(n))-1)/2)
    while len(queue):
        level, node = queue.popleft()
        if not node:
            continue
        if level != prev_level:
            tree_width = int(tree_width/2)
            print()
        print(' '*tree_width, end='')
        print(str(node.value), end='')
        queue.append((level+1, node.left))
        queue.append((level+1, node.right))
        prev_level = level


'''
create_bst([0, 1, 2, 3], root)
root.value = 2
    create_bst([0, 1], root.left)
    root.left.value = 1
        create_bst([0], root.left.left)
        root.l.l.value = 0
    create_bst([3], root.right)
    root.right.value = 3
'''
def create_bst(array: list, parent: Node) -> None:
    mid = len(array) // 2
    parent.value = array[mid]
    if array[:mid]:
        parent.left = Node(0)
        create_bst(array[:mid], parent.left)
    if mid+1 < len(array):
        parent.right = Node(0)
        create_bst(array[mid+1:], parent.right)


def create_bs_tree(array: list) -> Node:
    root = Node(0)
    create_bst(array, root)
    return root


if __name__ == '__main__':
    array = list(range(3))
    tree = create_bs_tree(array)
    print_tree(tree, len(array))

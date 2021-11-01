'''
Validate if a binary tree is a binary search tree.

Solution:

Binary tree is a BST if for each node, max value of left subtree is <= node.value and min value of right subtree > node.value

Brute force:
For each node, find max of left subtree, and min of right subtree and check the condition. This gives O(N)=N^2

Better solution:
Iterate the binary tree in-order (left node, parent, right node) and append nodes to the list. Check that list is sorted.
time: O(N)=N
space: O(N)=N

          5
        3   7
      1  4 6  8

1 3 4 5 6 7 8
'''

from minimal_tree import create_bs_tree
from minimal_tree import Node


def traverse_in_order(root: Node, nodes: list) -> None:
    if not root:
        return
    traverse_in_order(root.left, nodes)
    nodes.append(root.value)
    traverse_in_order(root.right, nodes)


class NoExtraSpaceSolution:
    def __init__(self, root: Node):
        self.root = root
        self.last = None

    def traverse_and_compare(self, root: Node) -> bool:
        if not root:
            return True

        if not self.traverse_and_compare(root.left):
            return False

        if self.last and root.value <= self.last.value:
            return False

        self.last = root

        if not self.traverse_and_compare(root.right):
            return False

        return True

    def solve(self) -> bool:
        return self.traverse_and_compare(self.root)


class MinMaxSolution:
    def __init__(self, root: Node):
        self.root = root

    def __solve(self, node: Node, min: int, max: int) -> bool:
        if min is not None and node.value <= min:
            return False

        if max is not None and node.value > max:
            return False

        if node.left and not self.__solve(node.left, min, node.value):
            return False

        if node.right and not self.__solve(node.right, node.value, max):
            return False

        return True

    def solve(self) -> bool:
        return self.__solve(self.root, None, None)


def is_bst(root: Node) -> bool:
    nodes = []
    traverse_in_order(root, nodes)
    print(*nodes)
    prev = nodes[0]
    for n in nodes[1:]:
        if n < prev:
            return False
        prev = n
    return True


if __name__ == '__main__':
    bs_tree = create_bs_tree(list(range(16)))
    assert is_bst(bs_tree)
    assert NoExtraSpaceSolution(bs_tree).solve()
    assert MinMaxSolution(bs_tree).solve()
    root = Node(1)
    root.left = Node(5)
    root.right = Node(6)
    root.left.left = Node(-1)
    root.right.right = Node(2)
    assert not is_bst(root)
    assert not NoExtraSpaceSolution(root).solve()
    assert not MinMaxSolution(root).solve()

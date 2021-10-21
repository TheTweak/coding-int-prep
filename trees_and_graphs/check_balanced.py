'''
Implement an algorithm to check if a binary tree is balanced. For the purposes
of this question a balanced tree is defined such that the heights of the two
subtrees of any node never differ by more than one.

brute force:
    1) implement a function to calc the height of a tree
    2) starting from the root calculate H_left and H_right, compare them, if diff > 1, then tree is unbalanced
    3) continue with root.left and root.right

    this gives O(N)=N^2, which is not optimal

    re-use calculated subtree heights as we go up the tree

    height(subtree) = max(height(subtree.left), height(subtree.right)) + 1
    height(null node) = 0
    dict[subtree] = height
'''
from minimal_tree import create_bs_tree
from minimal_tree import Node


def is_balanced_(root: Node, heights: dict) -> (bool, int):
    if not root:
        return True, 0
    if root.value in heights:
        return heights[root.value]
    left_is_b, left_height = is_balanced_(root.left, heights)
    right_is_b, right_height = is_balanced_(root.right, heights)
    height = max(left_height, right_height) + 1
    balanced = abs(left_height - right_height) <= 1
    heights[root.value] = (balanced, height)
    return heights[root.value]


def is_balanced(root: Node) -> bool:
    return is_balanced_(root, {})


def create_unbalanced_btree() -> Node:
    root = Node(0)
    left = Node(1)
    root.left = left
    root.right = Node(3)
    left.left = Node(4)
    left.left.left = Node(5)
    left.left.left.left = Node(6)
    return root


if __name__ == '__main__':
    array = list(range(7))
    bstree = create_bs_tree(array)
    is_b, height = is_balanced(bstree)
    assert is_b
    print(f'height is {height}')
    is_b, height = is_balanced(create_unbalanced_btree())
    assert not is_b
    print(f'height is {height}')

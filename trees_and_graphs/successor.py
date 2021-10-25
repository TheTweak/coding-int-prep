'''
Implement an algorithm to find the "next" node (i.e. in-order successor of a given node) in a BST.
You may assume that each node has a link to its parent node.

Solution:

               5
        3           7
    1      4      6      8
  -1   3.5 4.5 5.5 6.5


 successor(5) = 5.5
 successor(1) = 3
 successor(4) = 4.5

 if has right child:
     - left most child to the right
 else if this node is a left child:
     - its parent
 else if this node is a right child:
     - its parent's parent

time: O(N)=logN if tree is balanced, else N
space: O(N)=logN if tree is balanced, else N
'''

from minimal_tree import Node

class NodeWithParent(Node):
    def __init__(self, value, parent=None):
        super().__init__(value)
        self.parent = parent


def create_bst(array: list, parent: NodeWithParent) -> None:
    mid = len(array) // 2
    parent.value = array[mid]
    if array[:mid]:
        parent.left = NodeWithParent(0, parent)
        create_bst(array[:mid], parent.left)
    if mid+1 < len(array):
        parent.right = NodeWithParent(0, parent)
        create_bst(array[mid+1:], parent.right)


def create_bs_tree(array: list) -> NodeWithParent:
    root = NodeWithParent(0)
    create_bst(array, root)
    return root

def leftmost(node: NodeWithParent) -> NodeWithParent:
    if not node.left:
        return node
    return leftmost(node.left)

def successor(node: NodeWithParent) -> int:
    if node.right:
        return leftmost(node.right).value
    elif node.parent.left is node:
        return node.parent.value
    elif node.parent.right is node:
        return node.parent.parent.value
    return -1


if __name__ == '__main__':
    bstree = create_bs_tree(list(range(16)))
    root = bstree
    leftmost_node = root
    while True:
        if leftmost_node.left:
            leftmost_node = leftmost_node.left
        else:
            break
    right_child = root.right.left.right

    print(f'root is {root.value}')
    print(f'leftmost_node is {leftmost_node.value}')
    print(f'right is {right_child.value}')

    assert successor(root) == 9
    assert successor(leftmost_node) == 1
    assert successor(right_child) == 12

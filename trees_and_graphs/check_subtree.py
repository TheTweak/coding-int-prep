'''
T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an algorithm to
determine if T2 is a subtree of T1.
A tree T2 is a subtree of T1 if there exists a node N in T1 such that the subtree of N is
identical to T2. That is, if you cut off the tree at node N, the two trees would be equal.

Brute force:

start with root in T1, check if left node is equal to root of T2 .. etc, compare all nodes
then check right node.
then do the same with left, and right nodes as root

time: O(N)=M*N, M-nodes in T1, N-nodes in T2

compare two trees:

check if root A == root B
recursively check root.left == root.right

Improvement:

flatten the tree to set (or multiset if non distinct elements)
then compare two sets of nodes
'''
from minimal_tree import Node

'''
        0
    1       2
  3   4   5   6
'''
def create_T1() -> Node:
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)

    root.left.left = Node(3)
    root.left.right = Node(4)

    root.right.left = Node(5)
    root.right.right = Node(6)
    return root


'''
   2
5     6
'''
def create_T2_subtree() -> Node:
    root = Node(2)
    root.left = Node(5)
    root.right = Node(6)
    return root


def create_T2_notsubtree() -> Node:
    root = create_T2_subtree()
    root.right.right = Node(10)
    return root

class RecursiveSolution:
    def __init__(self, t1: Node, t2: Node):
        self.t1 = t1
        self.t2 = t2

    def tree_equal(self, a: Node, b: Node) -> bool:
        if not a and not b:
            return True
        if (a is None and b is not None) or \
            (b is None and a is not None) or \
            a.value != b.value:
            return False
        return self.tree_equal(a.left, b.left) and \
            self.tree_equal(a.right, b.right)

    def check_subtree(self, t1: Node, t2: Node) -> bool:
        if self.tree_equal(t1.left, t2) or \
            self.tree_equal(t1.right, t2):
            return True
        result = False
        if t1.left:
            result |= self.check_subtree(t1.left, t2)
        if t1.right:
            result |= self.check_subtree(t1.right, t2)
        return result

    def solve(self) -> bool:
        return self.check_subtree(self.t1, self.t2)

'''
1. Flatten the trees
2. Search T2 subsequence in T1

time O(N)=len(T1)
space O(N)=M+N
'''
class IterativeSolution:
    def __init__(self, t1: Node, t2: Node):
        self.t1 = t1
        self.t2 = t2

    def flatten_tree(self, root: Node, result: list) -> None:
        if not root:
            return
        self.flatten_tree(root.left, result)
        result.append(root.value)
        self.flatten_tree(root.right, result)

    def solve(self) -> bool:
        t1_flat = []
        self.flatten_tree(self.t1, t1_flat)
        t2_flat = []
        self.flatten_tree(self.t2, t2_flat)
        p1 = 0
        p2 = 0
        while p1 < len(t1_flat) and p2 < len(t2_flat):
            n1 = t1_flat[p1]
            n2 = t2_flat[p2]
            p1 += 1
            if n1 == n2:
                p2 += 1
            else:
                p2 = 0
        if p2 == len(t2_flat):
            return True
        return False

if __name__ == '__main__':
    t1 = create_T1()
    t2_subtree = create_T2_subtree()
    assert RecursiveSolution(t1, t2_subtree).solve()
    t2_notsubtree = create_T2_notsubtree()
    assert not RecursiveSolution(t1, t2_notsubtree).solve()

    assert IterativeSolution(t1, t2_subtree).solve()
    assert not IterativeSolution(t1, t2_notsubtree).solve()

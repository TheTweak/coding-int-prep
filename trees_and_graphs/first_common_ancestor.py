'''
Write an algorithm to find a first common ancestor of two nodes in a binary tree.
Avoid storing additional nodes in a data structure. This is not necessary a BST.

Solution:

            a
        b       c
    d      e   f  g
  h  x    i    j     k
    l   n

fca(l, i)=b
fca(k, n)=a

Brute force:

if parent link is available:

common ancestor means both A and B are reachable from it. Start from parent of A,
then check parent of B. Then A parent's parent, etc.

if not:
    start from root

time: O(N)=N^2

improvement:

cache is_reachable result, reduces O(N)=N
'''

class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


def is_reachable(a: Node, b: Node, cache: dict) -> bool:
    if a in cache and b in cache[a]:
        return cache[a][b]
    if a is b:
        cache.setdefault(a, {})[b] = True
        return True
    result = False
    if a.left:
        result |= is_reachable(a.left, b, cache)
    if not result and a.right:
        result |= is_reachable(a.right, b, cache)
    cache.setdefault(a, {})[b] = False
    return result


def fca(root: Node, a: Node, b: Node) -> (bool, Node | None):
    cache = {}
    is_r, n = (False, None)
    if root.left:
        is_r, n = fca(root.left, a, b)
        if is_r:
            return is_r, n
    if root.right:
        is_r, n = fca(root.right, a, b)
        if is_r:
            return is_r, n
    if is_reachable(root, b, cache) and is_reachable(root, a, cache):
        return True, root
    return False, None


if __name__ == '__main__':
    root = Node('a')
    root.left = Node('b')
    b = root.left
    root.right = Node('c')
    c = root.right
    b.left = Node('d')
    b.left.right = Node('x')
    b.right = Node('e')
    c.left = Node('f')
    c.right = Node('g')
    d = b.left
    d.left = Node('h')
    d.left.right = Node('l')
    e = b.right
    e.left = Node('i')
    e.left.left = Node('n')
    c.left.left = Node('j')
    c.right.right = Node('k')

    _, fca_b = fca(root, d.left.right, e.left)
    print(fca_b.name)
    assert fca_b.name == 'b'
    _, fca_a = fca(root, c.right.right, e.left.left)
    print(fca_a.name)
    assert fca_a.name == 'a'

    _, fca_3 = fca(root, c.left, c.right)
    assert fca_3.name == 'c'

    _, fca_x = fca(root, d.left.right, b.left.right)
    assert fca_x.name == 'd'

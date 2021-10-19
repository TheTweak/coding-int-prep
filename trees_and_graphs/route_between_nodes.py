'''
Given a directed graph, and two nodes (S and E), design an algorithm to
find out whether there is a route from S to E.

Brute force:

do a BFS from S to find all nodes reachable from S

O(N)=V
'''

from collections import deque


class Node:
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def add(self, child) -> None:
        self.children.append(child)


def create_digraph() -> Node:
    root = Node('S')
    root.add(Node('F'))
    root.add(Node('G'))
    root.add(Node('H'))
    j = Node('J')
    root.add(j)
    j.add(Node('I'))
    j.add(Node('L'))
    k = Node('K')
    k.add(Node('Ka'))
    j.add(k)
    d = Node('D')
    j.add(d)
    d.add(Node('E'))
    return root


def is_connected(a: Node, b: str) -> bool:
    visited = set()
    nodes_queue = deque()
    nodes_queue.append(digraph)
    while len(nodes_queue):
        n = nodes_queue.popleft()
        if n.name in visited:
            continue
        for cn in n.children:
            if cn.name == b:
                return True
            nodes_queue.append(cn)
        visited.add(n.name)
    return False


if __name__ == '__main__':
    digraph = create_digraph()
    assert is_connected(digraph, 'E')
    assert not is_connected(digraph, 'disconnected')

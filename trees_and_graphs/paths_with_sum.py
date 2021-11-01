'''
You are given a binary tree in which each node contains an integer value (which might be positive or negative).
Design an algorithm to count the number of paths that sum to a given value. The path does not need to start or end at
the root or a leaf, but it must go downwards.
'''

'''
Brute force:

- start BFS from root
- calculate sum
- when sum is found, increment result by 1 and start again from root's child nodes
- O(N^2) in both time and space
'''

from collections import deque

from minimal_tree import Node
from minimal_tree import create_bs_tree

class BruteForceSolution:
    def __init__(self, root: Node, target: int):
        self.root = root
        self.target = target

    def bfs(self, root: Node) -> int:
        queue = deque()
        queue.append((root, 0))
        count = 0
        while queue:
            node, sum = queue.popleft()
            if sum + node.value == self.target:
                count += 1
            elif sum + node.value < self.target:
                if node.left:
                    queue.append((node.left, sum+node.value))
                if node.right:
                    queue.append((node.right, sum+node.value))
        return count

    def __solve(self, node: Node) -> int:
        if not node:
            return 0
        count = self.bfs(node)
        count += self.__solve(node.left)
        count += self.__solve(node.right)
        return count

    def solve(self) -> int:
        return self.__solve(self.root)


if __name__ == '__main__':
    '''
            1
        2       3
      1   2   5   0
    1            1
    '''
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(1)
    root.left.right = Node(2)
    root.left.left.left = Node(1)
    root.right.left = Node(5)
    root.right.right = Node(0)
    root.right.right.left = Node(1)

    print(BruteForceSolution(root, 5).solve())
    print(BruteForceSolution(root, 10).solve())
    print(BruteForceSolution(root, 9).solve())

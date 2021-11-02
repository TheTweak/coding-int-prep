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

Improvement:


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


'''
Keep the running sum as we process the nodes.
Start with root node, traverse its child nodes,
calculate the sum.

        1 (1)
    2 (3)   3
  1(4)   2  -2   2
1(5)          -1
'''
class RunningSumSolution:
    def __init__(self, root: Node, target: int):
        self.root = root
        self.target = target
        self.running_sum_dict = {}

    def __solve(self, node: Node, running_sum: int) -> int:
        if not node:
            return 0

        running_sum += node.value
        paths = self.running_sum_dict.get(running_sum-self.target, 0)
        if running_sum == self.target:
            paths += 1
        if running_sum in self.running_sum_dict:
            self.running_sum_dict[running_sum] += 1
        else:
            self.running_sum_dict[running_sum] = 1

        paths += self.__solve(node.left, running_sum)
        paths += self.__solve(node.right, running_sum)

        self.running_sum_dict[running_sum] = max(0, self.running_sum_dict[running_sum]-1)
        return paths

    def solve(self) -> int:
        return self.__solve(self.root, 0)

if __name__ == '__main__':
    '''
            1 (1)
        2 (2, 3) 3 (3, 4)
      1(1, 3, 4)   2   5   0 (0, 3, 4)
    1 (1, 2, 4, 5)           1 (1, 4, 5)
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

    assert BruteForceSolution(root, 5).solve() == 4
    assert BruteForceSolution(root, 10).solve() == 0
    assert BruteForceSolution(root, 9).solve() == 1

    assert RunningSumSolution(root, 5).solve() == 4
    assert RunningSumSolution(root, 10).solve() == 0
    assert RunningSumSolution(root, 9).solve() == 1

'''
A BST was created by traversing through an array from left to right, and inserting each element.
Given a BST with distinct elements, print all possible arrays that could have led to this tree.

Example:

input:

        2
    1       3
0    1.5 2.5  4

output: {2, 1, 3, 0, 1.5, 2.5, 4}, {2, 3, 1, 0, 1.5, 2.5, 4},
{2, 1, 3, 1.5, 0, 2.5, 4}

N nodes, possible arrays
1, 1
2, 1
3, 2
4, 2
5, 4
6,

on each full level, starting with 1st (0 based), we add X possible variants:
X=2^l!

total=1
for l in levels:
    total *= 2^l!

Solution:

- traverse the tree in pre-order (root first, then left, then right)
- on each level, take solutions from previous level and for each of them, append new solutions
- root has one solution = [root]

O(N)=N!
'''

from itertools import permutations

from minimal_tree import Node
from minimal_tree import create_bs_tree


def fill_levels(root: Node, level: int, levels: dict[int, list[Node]]) -> None:
    if not root:
        return
    levels.setdefault(level, []).append(root.value)
    fill_levels(root.left, level+1, levels)
    fill_levels(root.right, level+1, levels)


def bst_sequences(root: Node) -> list[list]:
    levels = {}
    fill_levels(root, 0, levels)
    solutions = {}
    for level, nodes in levels.items():
        if level == 0:
            solutions[0] = [nodes]
            continue
        prev_level = level-1
        prev_solutions = solutions[prev_level]
        for ps in prev_solutions:
            level_nodes = levels[level]
            for perm in permutations(level_nodes):
                new_solution = ps + list(perm)
                solutions.setdefault(level, []).append(new_solution)
    return solutions.popitem()[1]


if __name__ == '__main__':
    bst = create_bs_tree(list(range(9)))
    solutions = bst_sequences(bst)
    print(solutions)

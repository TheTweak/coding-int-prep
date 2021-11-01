'''
You are implementing a BST class from scratch which, in addition to insert, find, and delete, has a method
get_random_node() which returns a random node from the tree. All nodes should be equally likely to be chosen.
Design and implement an algorithm for get_random_node(), and explain how you would implement the rest of the methods.
'''


'''
Solution:

1) store BST in a flat array; use uniform_random(0, len(arr)) to return random node
2) if BST is represented as nodes, assign 2d coordinates (left hops, right hops) to each node (root is (0, 0))
then pick uniform_random(0, tree_height). But it requires tree to be balanced.
'''

from random import randint

from minimal_tree import Node

class BSTFlat:
    def __init__(self):
        self.init_capacity = 32
        self.nodes = [None for _ in range(self.init_capacity)]

    def __get_li(self, idx: int) -> int:
        return 2*idx+1

    def __get_ri(self, idx: int) -> int:
        return 2*idx+2

    def __grow(self, to_idx: int) -> None:
        self.nodes.extend([None for _ in range(to_idx-len(self.nodes)+1)])

    def __assign(self, idx: int, value: int) -> None:
        if idx >= len(self.nodes):
            self.__grow(idx)
        self.nodes[idx] = value

    def __insert(self, ni: int, value: int) -> None:
        if value > self.nodes[ni]:
            ri = self.__get_ri(ni)
            if ri < len(self.nodes) and self.nodes[ri] is not None:
                self.__insert(ri, value)
            else:
                self.__assign(ri, value)
        else:
            li = self.__get_li(ni)
            if li < len(self.nodes) and self.nodes[li] is not None:
                self.__insert(li, value)
            else:
                self.__assign(li, value)

    def insert(self, value: int) -> None:
        if self.nodes[0] is None:
            self.nodes[0] = value
            return
        self.__insert(0, value)

    def __find(self, node_idx: int, value: int) -> int | None:
        if node_idx >= len(self.nodes):
            return None

        node_val = self.nodes[node_idx]
        if node_val is None:
            return None

        if  node_val == value:
            return node_idx

        if value > node_val:
            return self.__find(self.__get_ri(node_idx), value)
        else:
            return self.__find(self.__get_li(node_idx), value)

    def find(self, value: int) -> int | None:
        return self.__find(0, value)

    def __delete(self, node_idx: int) -> None:
        left = self.__get_li(node_idx)
        if left >= len(self.nodes):
            self.nodes[node_idx] = None
            return

        self.nodes[node_idx] = self.nodes[left]
        self.__delete(left)

    def delete(self, value: int) -> bool:
        node_idx = self.find(value)
        if node_idx is None:
            return False
        self.__delete(node_idx)
        return True

    def get_random_node(self) -> int:
        rnode = self.nodes[randint(0, len(self.nodes)-1)]
        if rnode is None:
            return self.get_random_node()
        return rnode


if __name__ == '__main__':
    bst_flat = BSTFlat()
    bst_flat.insert(3)
    bst_flat.insert(1)
    bst_flat.insert(0)
    bst_flat.insert(2)
    bst_flat.insert(5)
    bst_flat.insert(4)
    bst_flat.insert(6)
    print(*bst_flat.nodes)
    print('Find:')
    print(bst_flat.find(6))
    print(bst_flat.find(5))
    print(bst_flat.find(4))
    print('Delete:')
    print(bst_flat.delete(1))
    print(bst_flat.delete(7))
    print(*bst_flat.nodes)
    print('Random:')
    print(bst_flat.get_random_node())
    print(bst_flat.get_random_node())
    print(bst_flat.get_random_node())
    print(bst_flat.get_random_node())
    print(bst_flat.get_random_node())
    print(bst_flat.get_random_node())
    print(bst_flat.get_random_node())
    print(bst_flat.get_random_node())
    print(bst_flat.get_random_node())
    print(bst_flat.get_random_node())

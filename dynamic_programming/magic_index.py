'''
A magic index in an array A is defined to be an index such that A[i] = i.
Given a sorted array of distinct integers, write a method to find such index if one exists.

FOLLOW UP: what if the values are not distinct?

A = [5 6 7 8]
A = [1 2 3]
A = [0 1 2 3]
A = [0 2 3 4 5]
A = [-2 -1 2]

if the values are not distinct:

    A = [1 1 2 3] i = 1
    A = [0 0 0 3] i = 3
    A = [5 5 6 x x x 6] l=7
'''

def find_magic_index_distinct(a: list[int]) -> int:
    for i, x in enumerate(a):
        if i == x:
            return i
        
        if x > i:
            break
    
    return -1


def find_magic_index(a: list[int]) -> int:
    for i, x in enumerate(a):
        if i == x:
            return i

        if x >= len(a):
            break
    
    return -1


if __name__ == '__main__':
    assert find_magic_index_distinct([0, 1, 2, 3]) == 0
    assert find_magic_index_distinct([-1, -2, 2, 3]) == 2
    assert find_magic_index_distinct([2, 3, 4, 5]) == -1

    assert find_magic_index([1, 2, 2, 2, 4]) == 2
    assert find_magic_index([4, 4, 4, 4, 4]) == 4
    assert find_magic_index([4, 5, 5, 5, 5]) == -1
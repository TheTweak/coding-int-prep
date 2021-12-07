'''
A magic index in an array A is defined to be an index such that A[i] = i.
Given a sorted array of distinct integers, write a method to find such index if one exists.

FOLLOW UP: what if the values are not distinct?

A = [5 6 7 8]
A = [1 2 3]
A = [0 1 2 3]
A = [0 2 3 4 5]
A = [-2 -1 2]
A = [0 1 5 6 9]
     0 1 2 3 4

l=0 r=5 mid=2, a[mid]>mid
l=0 r=2 mid=1, a[mid]==mid

a=[5 6 7 8 9 10]
l=0 r=6 mid=3 a[mid]>mid
l=0 r=3 mid=1 a[mid]>mid
l=0 r=1 mid=0 a[mid]>mid
l=0 r=0 return -1

a=[-5 -4 -3 -2 -1 5]
l=0 r=6 mid=3 a[mid]<mid
l=3 r=6 mid=4 a[mid]<mid
l=4 r=6 mid=5 a[mid]==mid 



if the values are not distinct:

    A = [1 1 2 3] i = 1
    A = [0 0 0 3] i = 3
    A = [5 5 6 x x x 6] l=7
'''

def bin_search(a: list, x:int, l: int, r: int) -> int:
    if l > r:
        return -1

    mid = (l + r) // 2
    if a[mid] == x:
        return mid

    if a[mid] > x:
        return bin_search(a, x, l, mid-1)
    else:
        return bin_search(a, x, mid+1, r)

def find_magic_index_distinct_(a: list[int], l: int, r: int) -> int:
    if l >= r:
        return -1

    mid = (l + r) // 2
    if a[mid] == mid:
        return mid

    if a[mid] > mid:
        return find_magic_index_distinct_(a, l, mid)
    else:
        return find_magic_index_distinct_(a, mid, r)


def find_magic_index_distinct(a: list[int]) -> int:
    return find_magic_index_distinct_(a, 0, len(a))


def find_magic_index(a: list[int]) -> int:
    return find_magic_index_distinct_(a, 0, len(a))


if __name__ == '__main__':
    print(find_magic_index_distinct([0, 1, 2, 3]))
    print(find_magic_index_distinct([-1, -2, 2, 3]))
    print(find_magic_index_distinct([2, 3, 4, 5]))

    print(find_magic_index([1, 2, 2, 2, 4]))
    print(find_magic_index([4, 4, 4, 4, 4]))
    print(find_magic_index([4, 5, 5, 5, 5]))

    a = [5, 6, 7, 10, 12, 14, 100]
    assert bin_search(a, 0, 0, len(a)-1) == -1
    assert bin_search(a, 5, 0, len(a)-1) == 0
    assert bin_search(a, 14, 0, len(a)-1) == 5
    assert bin_search(a, 100, 0, len(a)-1) == 6
    assert bin_search(a, 10, 0, len(a)-1) == 3
'''
Given a sorted array of n integers that has been rotated an unknown number of times, write code
to find an element in the array. Array was originally sorted in the increasing order.

Example:

find 5 in [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]

output: 8
'''
import sys


def find_offset(a: list[int]) -> int:
    min_el = sys.maxsize
    min_i = 0
    i = 0
    for x in a:
        if x < min_el:
            min_i = i
            min_el = x
        i += 1

    return min_i


def get_orig_idx(i: int, offset: int, size: int) -> int:
    return (i + offset) % size


def bin_search(a: list[int], el: int, l: int, h: int, offset: int) -> int:
    if l > h:
        return -1

    mid = (l + h) // 2
    mid_ = get_orig_idx(mid, offset, len(a))
    if a[mid_] == el:
        return mid_
    elif a[mid_] > el:
        return bin_search(a, el, l, mid - 1, offset)
    else:
        return bin_search(a, el, mid + 1, h, offset)


def search_rotated(a: list[int], el: int) -> int:
    offset = find_offset(a)
    return bin_search(a, el, 0, len(a), offset)
    

if __name__ == '__main__':
    a = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    result = search_rotated(a, 5)
    print(f'result: {result}')
    assert result == 8

    result = search_rotated(a, 100)
    print(f'result: {result}')
    assert result == -1

    result = search_rotated(a, 1)
    print(f'result: {result}')
    assert result == 5


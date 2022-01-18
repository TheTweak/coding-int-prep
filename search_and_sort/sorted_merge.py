'''
You are given two sorted arrays, A and B, where A has enough buffer in the end to
accomodate all B. Write a method to merge B into A in sorted order.
'''

def shift_right(x: list[int], start: int) -> None:
    prev = None
    for i in range(start, len(x)):
        tmp = x[i]
        x[i] = prev
        prev = tmp


def sorted_merge_shift(a: list[int], b: list[int]) -> None:
    '''
    time complexity O(n*m)
    '''
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] and a[i] > b[j]:
            shift_right(a, i)
            a[i] = b[j]
            j += 1
        i += 1

    if j != len(b):
        a[i-(len(b)-j):] = b[j:]


def sorted_merge_backwards(a: list[int], b: list[int]) -> None:
    '''
    time complexity O(n+m)
    '''
    i = -1
    for x in a:
        if x is None:
            break
        i += 1
    j = len(b) - 1
    k = len(a) - 1

    while j >= 0:
        if i >= 0 and a[i] >= b[j]:
            a[k] = a[i]
            i -= 1
        else:
            a[k] = b[j]
            j -=1
        k -= 1

        
if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, None, None, None, None, None, None]
    b = [0, 2, 3, 6, 8, 10]
    sorted_merge_backwards(a, b)
    assert a == [0, 1, 2, 2, 3, 3, 4, 5, 6, 8, 10]

    a = [1, 2, 3, 4, 5, None, None, None, None, None, None]
    b = [10, 11, 12, 13, 14, 15]
    sorted_merge_backwards(a, b)
    assert a == [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15]

    a = [1, 2, 3, 4, 5, None, None, None, None, None, None]
    b = [-10, -9, -8, -7, -6, -5]
    sorted_merge_backwards(a, b)
    assert a == [-10, -9, -8, -7, -6, -5, 1, 2, 3, 4, 5]

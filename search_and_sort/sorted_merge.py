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


def sorted_merge(a: list[int], b: list[int]) -> None:
    '''
        a = [1, 2, 3, 4, 5, None, None, None, None, None, None]
        b = [0, 2, 3, 6, 8, 10]

        i = 0, j = 0
        a = [0, 1, 2, 3, 4, 5, None, None, None, None, None]

        i = 1, j = 1
        a = [0, 1, 2, 3, 4, 5, None, None, None, None, None]

        i = 3, j = 1
        a = [0, 1, 2, 2, 3, 4, 5, None, None, None, None]

        i = 5, j = 2
        a = [0, 1, 2, 2, 3, 3, 4, 5, None, None, None]
        
        i = 6, j = 3
        a = [0, 1, 2, 2, 3, 3, 4, 5, None, None, None]

        i = 10
        a[8:] = b[3:]
        
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

        
if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, None, None, None, None, None, None]
    b = [0, 2, 3, 6, 8, 10]
    sorted_merge(a, b)
    assert a == [0, 1, 2, 2, 3, 3, 4, 5, 6, 8, 10]

    a = [1, 2, 3, 4, 5, None, None, None, None, None, None]
    b = [10, 11, 12, 13, 14, 15]
    sorted_merge(a, b)
    assert a == [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15]

    a = [1, 2, 3, 4, 5, None, None, None, None, None, None]
    b = [-10, -9, -8, -7, -6, -5]
    sorted_merge(a, b)
    assert a == [-10, -9, -8, -7, -6, -5, 1, 2, 3, 4, 5]

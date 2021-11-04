'''
Given a positive integer, print the next smallest and the next largest number
that have the same number of 1 bits in their binary representation.

Brute force:

- convert to bits (4)
- 0000100
- shift left - next largest 0001000 (16)
- shift right - next smallest 0000010 (2)
- corner case - 0001 - next smallest is (-1)
- corner case - overflow with largest number
'''

def next_number(x: int) -> (int, int):
    return -1 if x==1 else x >> 1, x << 1

if __name__ == '__main__':
    solution = next_number(4)
    assert solution == (2, 8)
    assert next_number(1) == (-1, 2)

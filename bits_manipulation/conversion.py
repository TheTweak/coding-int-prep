'''
Write a function to determine the number of bits you need to flip, to get integer A from B.

Ex.:
Input: 29 (11101), 15 (01111)
Output: 2

Brute force:

For each bit in A, check if B has the same bit. If not, increment the count.

11101
01111

10010

Better algorithm:

XOR the numbers. Count the 1s in the result.
'''


def conversion(a: int, b: int) -> int:
    c = a ^ b
    flip_bits = 0
    while c:
        if c & 1:
            flip_bits += 1
        c = c >> 1
    return flip_bits


if __name__ == '__main__':
    assert conversion(29, 15) == 2

'''
Given a positive integer, print the next smallest and the next largest number
that have the same number of 1 bits in their binary representation.

get_next:

n=1432

10 9 8 7 6 5 4 3 2 1 0
 1 0 1 1 0 0 1 1 0 0 0

 to increase the number flip i to 1 and j to 0, where i>j

 "i" should be the rightmost non-trail 0, because only in this case
 we have 1s to flip back without decreasing the number more than
 increasing it. i=5

10 9 8 7 6 5 4 3 2 1 0
 1 0 1 1 0 1 1 1 0 0 0

 n=1464

 now we have too many 1s, we need to flip one of the 1s to the right of i=5
 and to make the number as small as possible. To do that we can re-arrange
 bits to the right of "i" so that 1s go first, and also remove one of the 1s.
 "c1" - number of 1s to the right of "i"

 1) reset bits to the right of "i"
 2) add c1-1 1s starting from rightmost bit

10 9 8 7 6 5 4 3 2 1 0
 1 0 1 1 0 1 0 0 0 0 1

get_prev:

n=1432

10 9 8 7 6 5 4 3 2 1 0
 1 0 1 1 0 0 1 1 0 0 0

flip one of the 1s to 0, rightmost non-trailing 1, to make the number as big as possible,
but less than N
               *
10 9 8 7 6 5 4 3 2 1 0
 1 0 1 1 0 0 1 0 0 0 0

 now we have too many 0s, we need to flip one of the 0s to 1, to the right of 3
 and also re-arrange the 1s so that the number is as high as possible

1) reset bits to the right of "3" to 0
2) add c1+1 1s starting from the leftmost bit

10 9 8 7 6 5 4 3 2 1 0
 1 0 1 1 0 0 1 0 1 0 0
'''

from copy import copy


class Solution:
    def __init__(self, N):
        self.N = N
        self.bits = self.__get_bits()

    def __get_bits(self) -> list[int]:
        q = self.N
        r = 0
        bits = []
        while q:
            r = q % 2
            bits.append(1 if r else 0)
            q = q // 2
        return list(reversed(bits))

    def __inv(self, x) -> int:
        x_ = x
        bits = 0
        while x:
            bits += 1
            x = x >> 1
        ones = ((1 << bits)-1)
        return ones - x_

    def __get_next(self) -> int:
        n = self.N
        c0 = 0
        while (n & 1 == 0) and n != 0:
            c0 += 1
            n = n >> 1

        c1 = 0
        while n & 1 == 1:
            c1 += 1
            n = n >> 1

        rmost_zero = c1 + c0
        n = self.N
        n = n | (1 << rmost_zero)
        mask = self.__inv(1 << rmost_zero)
        print(f'n={bin(n)} mask={bin(mask-1)}')
        n = n & mask

        bits_copy = copy(self.bits)

        bits_copy[rmost_zero] = 1
        c1 = 0
        for i, bit in enumerate(self.bits[rmost_zero+1:]):
            if bit == 1:
                c1 += 1
                bits_copy[rmost_zero+1+i] = 0

        for i in range(len(bits_copy)-c1+1, len(bits_copy)):
            bits_copy[i] = 1

        return int(''.join([str(x) for x in bits_copy]), 2)

    def solve(self) -> (int, int):
        return 0, self.__get_next()

if __name__ == '__main__':
    p, n = Solution(1432).solve()
    print(n)
    assert  p, n == (1428, 1441)

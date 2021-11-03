'''
You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to insert M
into N such that M starts at bit j and ends at bit i. You can assume that the bits j through i have enough
space to fit all of M.
'''

class Solution:
    def __init__(self, N: int, M: int, i: int, j: int):
        self.N = N
        self.M = M
        self.i = i
        self.j = j

    def get_ith_bit(self, x: int, i: int) -> int:
        mask = (1 << i)
        return x & mask

    def set_ith_bit(self, x: int, i: int) -> int:
        mask = (1 << i)
        return x | mask

    def unset_ith_bit(self, x: int, i: int) -> int:
        mask = ~(1 << i)
        return x & mask

    def solve(self) -> str:
        k = self.j - self.i
        result = self.N
        for x in range(self.j, self.i-1, -1):
            if self.get_ith_bit(self.M, k):
                result = self.set_ith_bit(result, x)
            else:
                result = self.unset_ith_bit(result, x)
            k -= 1
        return str(bin(result))


def from_bits(bits: str) -> int:
    return int(bits, 2)


if __name__ == '__main__':
    solution = Solution(from_bits('10000000000'), from_bits('10011'), 2, 6).solve()
    print(solution)
    assert  solution == '0b10001001100'

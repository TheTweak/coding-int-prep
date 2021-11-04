'''
Given a real number between 0 and 1, that is passed in as a float, print the binary
representation. If the number can not be represented accurately with at most 32
characters, print ERROR.
'''


class Solution:
    def __init__(self, n: float):
        self.n = n
        self.total_chars = 32

    def __get_digit_count(self, x):
        str_x = str(x)
        str_x = str_x.split('.')[1]
        return len(str_x)

    def __to_bin(self, x: int) -> list[int]:
        q = x
        r = 0
        bits = []
        while True:
            q_ = q // 2
            r = q % 2
            if not r:
                bits.append(0)
            else:
                bits.append(1)
            if not q_:
                break
            q = q_
        return [str(b) for b in reversed(bits)]

    '''
    format = mantiss X 10^-Z

    0.72 = 72 X 10^-2

    72 / 2 = 36             1001000
    36 / 2 = 18
    18 / 2 = 9
    9 / 2 = 4 (1)
    4 / 2 = 2
    2 / 2 = 1
    1 / 2 = 0
    '''
    def solve(self) -> str:
        digits = self.__get_digit_count(self.n)
        mantiss = int(self.n*(10**digits))
        mantiss_bits = self.__to_bin(mantiss)
        exp_bits = self.__to_bin(digits)
        return ''.join(mantiss_bits) + ' ' + ''.join(exp_bits)

class Solution2:
    def __init__(self, n: float):
        self.n = n

    def solve(self) -> str:
        bits = []
        num = self.n
        while num > 0:
            if len(bits) > 32:
                return 'error'
            r = num * 2
            r = float(f'{r:.2f}')
            if r >= 1:
                bits.append('1')
                num = r - 1
            else:
                bits.append('0')
                num = r

        bits.append('.')
        return ''.join(reversed(bits))

if __name__ == '__main__':
    print(Solution(0.625).solve())
    print(Solution2(0.625).solve())

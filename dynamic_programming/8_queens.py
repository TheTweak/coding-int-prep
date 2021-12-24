'''
Write an algorithm to print all ways of arranging 8 queens on a 8x8 chess board.
Queens can't share the same diagonal, row, or column. Diagonal means all diagonals, not just
the two that bissect the whole board in 2 parts.

Board:

--------
--------
--------
--------
--------
--------
--------
--------

1.
q-------
--------
--------
--------
--------
--------
--------
--------

2.
q-------
--q-----
--------
--------
--------
--------
--------
--------

q-------
--q-----
----q---
------q-
---q----
-q------
-------q
-----q--

place_queen(board, row)

'''

class Solution:
    def __init__(self, board_size=8):
        self.board_size = board_size
        self.board = [[0 for _ in range(board_size)] for _ in range(board_size)]

    def __get_diag__(self, row, col) -> (int, int):
        return col-row, col+row

    def __print_board__(self) -> None:
        for r in self.board:
            print(*r)
        print()
            
    def __calc_ways__(self, row: int, cols_taken: list[int], diags_taken: dict[int:int]) -> int:
        if row == self.board_size:
            self.__print_board__()
            return 1

        result = 0

        for c in range(self.board_size):
            d1, d2 = self.__get_diag__(row, c)

            if row == 0 or \
               (cols_taken[c] == 0 and \
                (diags_taken.get(d1, 0) == 0 and diags_taken.get(d2, 0) == 0)):
                
                self.board[row][c] = 1
                cols_taken[c] = 1
                diags_taken[d1] = 1
                diags_taken[d2] = 1
                
                result += self.__calc_ways__(row+1, cols_taken, diags_taken)

                self.board[row][c] = 0
                cols_taken[c] = 0
                diags_taken[d1] = 0
                diags_taken[d2] = 0

        return result  
        
    def solve(self) -> int:
        return self.__calc_ways__(0, \
            [0 for _ in range(self.board_size)], \
            {})


if __name__ == '__main__':
    print(Solution().solve())

'''
Design and implement a text-based minesweeper game.
'''

from enum import Enum
from random import randint

class CellType(Enum):    
    Number = 0,
    Bomb = 1


class Cell:
    def __init__(self, row: int, col: int, type: CellType, number: int = 0):
        self.type = type
        self.number = number
        self.hidden = True
        self.row = row
        self.col = col
        self.flagged = False

    def __str__(self) -> str:
        if self.flagged:
            return 'f'

        if self.hidden:
            return '?'

        if self.type is CellType.Number:
            return str(self.number) if self.number else ' '        
        
        return '*'        


class Board:
    def __init__(self, N: int, B: int):
        self.cells = [[Cell(row=r, col=c, type=CellType.Number) for c in range(N)] for r in range(N)]
        self.open_cells = 0
        self.bombs_count = B
        bombs_created = 0
        while bombs_created != B:
            row = randint(0, N-1)
            col = randint(0, N-1)
            if self.cells[row][col].type is not CellType.Bomb:
                bombs_created += 1
                self.cells[row][col].type = CellType.Bomb
                self.__mark_neighbour_nums(row, col, N)

    def check_win(self) -> int:
        hidden_cells = 0
        for row in self.cells:
            for c in row:
                if c.hidden:
                    hidden_cells += 1
        if hidden_cells == self.bombs_count:
            return 1
        return 0

    def click_cell(self, row: int, col: int) -> int:
        assert 0 <= row < len(self.cells) and 0 <= col < len(self.cells)

        cell = self.cells[row][col]
        cell.hidden = False
        if cell.type is CellType.Bomb:
            return -1
        
        self.open_cells += 1
        if cell.number:
            return self.check_win()

        visited = set()
        queue = []
        queue.append((row, col))
        while len(queue):
            r, c = queue.pop()

            if (r, c) in visited:
                continue

            if (r, c) != (row, col):
                self.open_cells += 1

            visited.add((r, c))
            self.cells[r][c].hidden = False

            if self.cells[r][c].number:
                continue

            for c in self.__get_neighbours(r, c):
                if c.type is CellType.Bomb:
                    continue

                queue.append((c.row, c.col))
        return self.check_win()

    def __str__(self) -> str:
        result = ''
        for row in self.cells:
            result += ''.join(str(c) for c in row)
            result += '\n'
        return result

    def __get_neighbours(self, row: int, col: int) -> list[Cell]:
        N = len(self.cells)
        result = []
        if col > 0:
            # upper left
            if row > 0:
                result.append(self.cells[row-1][col-1])
                
            # left
            result.append(self.cells[row][col-1])
            # bottom left
            if row < N-1:
                result.append(self.cells[row+1][col-1])

        # upper
        if row > 0:
            result.append(self.cells[row-1][col])
                
        # down
        if row < N-1:
            result.append(self.cells[row+1][col])

        # upper right
        if col < N-1:
            if row > 0:
                result.append(self.cells[row-1][col+1])
            # right
            result.append(self.cells[row][col+1])
            # bottom right
            if row < N-1:
                result.append(self.cells[row+1][col+1])
        return result

    def __mark_neighbour_nums(self, row: int, col: int, N: int) -> None:
        neighbours = self.__get_neighbours(row, col)
        for n in neighbours:
            n.number += 1


class Minesweeper:
    def __init__(self, N: int, B: int):
        self.board = Board(N, B)

    def start(self) -> None:
        while True:
            print(self.board)
            row, col = input('select cell').split(' ')

            result = self.board.click_cell(int(row), int(col))
            if result < 0:
                print(self.board)
                print('You loose')
                return
            elif result > 0:
                print(self.board)
                print('You win')
                return


if __name__ == '__main__':
    minesweeper = Minesweeper(5, 2)
    minesweeper.start()
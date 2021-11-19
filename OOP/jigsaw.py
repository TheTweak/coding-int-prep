'''
Implement an NxN jigsaw puzzle. Design the data structures and explain an algorithm to solve the puzzle.
You can assume that you have a fitsWith method which, when passed two puzzle edges, returns true if the two
edges belong together.

questions:

1) how many people are solving the puzzle simultaneously?

how to solve:

1) find a left upper corner piece, put it in place
2) get all pieces with flat top, and try each one next to the upper left corner
3) now the top row is complete, this takes N^2
4) repeat for bottom row, leftmost column, rightmost column
5) then continue for inner square

time: O(N^2)
'''

from enum import Enum
from collections import namedtuple


Point = namedtuple('Point', 'row col')


class JigSawEdgeType(Enum):
    RShapedOut = 1,
    RShapedIn = 2,
    TShapedOut = 3,
    TShapedIn = 4,
    CShapedOut = 5,
    CShapedIn = 6,
    Plain = 7


class JigSawEdges:
    def __init__(self, top: JigSawEdgeType, right: JigSawEdgeType, bottom: JigSawEdgeType, left: JigSawEdgeType):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left


class JigSaw:
    def __init__(self, id: int, picture: str, edges: JigSawEdges):
        self.id = id
        self.picture = picture
        self.edges = edges

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: JigSaw) -> bool:
        return self.id == other.id


class Puzzle:
    def __init__(self, size: int):
        self.size = size
        self.remaining_pieces: set[JigSaw] = set()
        self.puzzle_board = [[None for _ in range(size)] for _ in range(size)]

    def get_remaining_piece(self) -> JigSaw:
        '''Returns random jigsaw from a set of remaining pieces'''
        pass

    def __get_neighbours(self, at: Point) -> set[JigSaw]:
        '''Returns neighbour (top, right, bottom, left) jigsaw pieces, if they exist'''
        pass

    def fits_with(self, a: JigSaw, b: JigSaw) -> bool:
        return True

    def insert_piece(self, piece: JigSaw, at: Point) -> bool:
        '''
        Inserts a piece into the puzzle and returns true if it fits with all of them.
        False otherwise.
        '''
        puzzle_board[at.row][at.col] = piece
        neighbours = self.__get_neighbours(at)
        for n in neighbours:
            if not self.fits_with(piece, n):
                return False

        return True

    def remove_piece(self, at: Point) -> JigSaw:
        '''Removes a piece from the puzzle and returns it'''
        pass

    def solved(self) -> bool:
        '''Returns true if a puzzle is solved. False otherwise'''
        pass

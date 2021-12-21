'''
Implement a paint fill function: chane the color of the point p and of the area of adjacent points with given color.

input: 2d array - picture, int - given color, (int, int) - given point

brute force:

- change color of point p
- change color for all adj points of same color

time O(n) - number adj of points of same color
memory O(n) - same
'''


class Painter:
    def __init__(self, img: list[list[int]], start_point: (int, int), color: int):
        self.img = img
        self.start_point = start_point
        self.orig_color = img[start_point[0]][start_point[1]]
        self.color = color
        self.cols = len(img[0])
        self.rows = len(img)
        self.adj = [(0, 1), (0, -1), (1, 0), (-1, 0), \
            (1, 1), (-1, 1), (-1, -1), (1, -1)]

    def __paint_fill__(self, point: (int, int)):
        row, col = point
        assert 0 <= row < self.rows
        assert 0 <= col < self.cols

        self.img[row][col] = self.color

        for ar, ac in self.adj:
            np_row, np_col = row + ar, col + ac
            if 0 <= np_row < self.rows and \
                0 <= np_col < self.cols and \
                self.img[np_row][np_col] == self.orig_color and \
                self.img[np_row][np_col] != self.color:
                
                self.__paint_fill__((np_row, np_col))
            
    def fill(self):
        self.__paint_fill__(self.start_point)
        

def print_img(img: list[list[int]]) -> None:
    for row in img:
        print(*row)
    print()
        

if __name__ == '__main__':
    img_white = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print_img(img_white)
    Painter(img_white, (1, 1), 2).fill()
    print_img(img_white)

    img_2 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print_img(img_2)
    Painter(img_2, (2, 3), 4).fill()
    print_img(img_2)

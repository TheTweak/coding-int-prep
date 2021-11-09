'''
A monochrome screen is stored as a single array of bytes, allowing eight consecutive pixels to be stored
in one byte. The screen has width w, where w is divisible by 8 (that is, no byte will be split across rows).
The height of screen, of course, can be derived from the length of the array and the width. Implement a
function that draws a horizontal line from (x1, y) to (x2, y):

draw_line(byte[] screen, int width, int x1, int x2, int y)


[00000000,
 00000000,
 00000000,
 00000011,
 11110000,
 00000000]

w=24 h=2


'''


def draw_line(screen: bytearray, width: int, x1: int, x2: int, y: int) -> None:
    height = len(screen)*8 // width

    assert y < height and \
        x1 < width and \
        x2 < width

    row_x1 = y * (width//8) + x1//8
    x1_mask = (1 << (8-(x1%8))) - 1
    screen[row_x1] |= x1_mask

    row_x2 = y * (width//8) + x2//8
    all_ones = (1 << 8) - 1
    x2_mask = all_ones - ((1 << (8-(x2%8)))-1)
    screen[row_x2] &= x2_mask
    screen[row_x2] |= x2_mask


if __name__ == '__main__':
    screen = bytearray(6)
    draw_line(screen, 24, 6, 12, 1)
    for row in screen:
        print(f'{row:8b}')

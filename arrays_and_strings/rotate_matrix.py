'''
Given an image, represented as a matrix NxN, write a method that rotates the image 90 degrees.
Can you do it in-place?
'''

def rotate90(image: list) -> list:
    n = len(image)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            result[c][n-r-1] = image[r][c]
    return result


def rotateN(s: int, n: int, i: int, arr: list) -> None:
    if s >= n:
        return
    a = arr[s+i][n]
    arr[s+i][n] = arr[s][s+i]
    b = arr[n][n-i]
    arr[n][n-i] = a
    c = arr[n-i][s]
    arr[n-i][s] = b
    arr[s][s+i] = c


def rotate90_inplace(image: list) -> None:
    n = len(image)
    for i in range(n):
        for j in range(n-1):
            rotateN(i, n-i-1, j, image)


def print_image(image: list) -> None:
    for row in image:
        print(' '.join([str(x) for x in row]))


if __name__ == '__main__':
    image = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
    print_image(image)
    print()

    expected = [[13, 9, 5, 1],
                [14, 10, 6, 2],
                [15, 11, 7, 3],
                [16, 12, 8, 4]]

    rotated = rotate90(image)
    print_image(rotated)
    print()
    assert rotated == expected

    rotate90_inplace(image)
    print_image(image)
    assert rotated == image


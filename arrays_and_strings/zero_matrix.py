'''
Write an algorithm, such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
'''

'''
for each r, c in m, if m[r][c] == 0
m[r][:] = 0
m[:][c] = 0
O(n) = m*n(m+n) + m*n
O(mn) space
'''
def zero_matrix(m: list) -> None:
    zero_ind = set()
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] == 0 and not (r, c) in zero_ind:
                for i in range(len(m[r])):
                    zero_ind.add((r, i))
                for i in range(len(m)):
                    zero_ind.add((i, c))
    for r, c in zero_ind:
        m[r][c] = 0


if __name__ == '__main__':
    matrix = [[1, 1, 1, 1],
              [1, 0, 1, 1],
              [1, 1, 1, 0]]

    zero_matrix(matrix)

    expected = [[1, 0, 1, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]

    print(matrix)

    assert matrix == expected

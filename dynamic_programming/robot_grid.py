'''
Imagine a robot sitting on the upper left corner of the grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are off limits
such that the robot can not step on them. Design an algorithm to find a path from the top
left to the bottom right.


'''

def find_path(grid: list[list[bool]]) -> list[(int, int)]:
    rows = len(grid)
    cols = len(grid[0])

    dp = [[(-1, -1) for _ in range(cols)] for _ in range(rows)]
    dp[0][0] = (0, 0)
    for r in range(rows):
        for c in range(cols):
            if dp[r][c] == (-1, -1):
                continue

            if c+1 < cols and grid[r][c+1]:
                dp[r][c+1] = (r, c)
            if r+1 < rows and grid[r+1][c]:
                dp[r+1][c] = (r, c)

    path = [(rows-1, cols-1)]
    x = dp[-1][-1]
    while True:
        path.append(x)
        if x[0] == 0 and x[1] == 0:
            break
        x = dp[x[0]][x[1]]
    return list(reversed(path))


if __name__ == '__main__':
    rows = 5
    cols = 5
    grid = [[True for _ in range(cols)] for _ in range(rows)]
    grid[1][0] = False
    grid[2][1] = False
    print(find_path(grid))